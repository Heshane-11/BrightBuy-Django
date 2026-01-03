from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseBadRequest
from carts.models import CartItem
from .forms import OrderForm
from django.conf import settings
import datetime, json, threading
from .models import Order, Payment, OrderProduct
from store.models import Product
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.db import transaction
from django.views.decorators.csrf import csrf_exempt

# ================= EMAIL HELPERS =================

class EmailThread(threading.Thread):
    def __init__(self, email):
        self.email = email
        super().__init__()

    def run(self):
        self.email.send()


@csrf_exempt
def payments(request):
    body = json.loads(request.body)
    print("🔥 PAYMENTS HIT:", body)

    order = Order.objects.get(
        user=request.user,
        is_ordered=False,
        order_number=body['orderID']
    )

    payment = Payment.objects.create(
        user=request.user,
        payment_id=body['transID'],
        payment_method=body['payment_method'],
        amount_paid=order.order_total,
        status=body['status'],
    )

    # ✅ ORDER MARK FIRST (FAST)
    order.payment = payment
    order.is_ordered = True
    order.status = 'Completed'
    order.save()

    # ✅ IMMEDIATE RESPONSE (Gunicorn safe)
    response = JsonResponse({
        'order_number': order.order_number,
        'transID': payment.payment_id,
    })

    # ================= POST PAYMENT TASKS =================
    def post_payment_tasks():
        # 🛒 cart → order products
        cart_items = CartItem.objects.filter(user=request.user)

        for item in cart_items:
            orderproduct = OrderProduct.objects.create(
                order=order,
                payment=payment,
                user=request.user,
                product=item.product,
                quantity=item.quantity,
                product_price=item.product.price,
                ordered=True,
            )
            orderproduct.variations.set(item.variations.all())

            item.product.stock -= item.quantity
            item.product.save()

        cart_items.delete()

        # 📧 EMAIL (THREAD)
        try:
            subject = "Thank you for your order!"
            message = render_to_string(
                "orders/order_recieved_email.html",
                {
                    "user": order.user,
                    "order": order,
                }
            )

            email = EmailMessage(
                subject,
                message,
                to=[order.email],
            )

            EmailThread(email).start()   # ⭐ MOST IMPORTANT LINE

            print("📧 EMAIL SENT")

        except Exception as e:
            print("❌ EMAIL ERROR:", e)

    # 🔥 RUN AFTER RESPONSE (NO BLOCKING)
    threading.Thread(target=post_payment_tasks).start()

    return response





def place_order(request, total=0, quantity=0):
    current_user = request.user
    cart_items = CartItem.objects.filter(user=current_user)

    if not cart_items.exists():
        return redirect('store')

    for item in cart_items:
        total += item.product.price * item.quantity
        quantity += item.quantity

    tax = (2 * total) / 100
    grand_total = total + tax

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(
                user=current_user,
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                phone=form.cleaned_data['phone'],
                email=form.cleaned_data['email'],
                address_line_1=form.cleaned_data['address_line_1'],
                address_line_2=form.cleaned_data['address_line_2'],
                country=form.cleaned_data['country'],
                state=form.cleaned_data['state'],
                city=form.cleaned_data['city'],
                order_note=form.cleaned_data['order_note'],
                order_total=grand_total,
                tax=tax,
                ip=request.META.get('REMOTE_ADDR'),
            )

            current_date = datetime.date.today().strftime("%Y%m%d")
            order.order_number = current_date + str(order.id)
            order.save()

            return render(request, 'orders/payments.html', {
                'order': order,
                'cart_items': cart_items,
                'total': total,
                'tax': tax,
                'grand_total': grand_total,
            })

    return redirect('checkout')


def order_complete(request):
    order_number = request.GET.get('order_number')
    transID = request.GET.get('payment_id')

    try:
        order = Order.objects.get(order_number=order_number, is_ordered=True)
        ordered_products = OrderProduct.objects.filter(order=order)
        payment = Payment.objects.get(payment_id=transID)

        subtotal = sum(i.product_price * i.quantity for i in ordered_products)

        return render(request, 'orders/order_complete.html', {
            'order': order,
            'ordered_products': ordered_products,
            'order_number': order.order_number,
            'transID': payment.payment_id,
            'payment': payment,
            'subtotal': subtotal,
        })

    except (Order.DoesNotExist, Payment.DoesNotExist):
        return redirect('home')
