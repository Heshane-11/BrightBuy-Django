from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from store.models import Product
from .models import Wishlist

@login_required(login_url='login')
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Wishlist.objects.get_or_create(
        user=request.user,
        product=product
    )
    return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='login')
def wishlist(request):
    items = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist/wishlist.html', {'items': items})

@login_required(login_url='login')
def remove_from_wishlist(request, product_id):
    Wishlist.objects.filter(user=request.user, product_id=product_id).delete()
    return redirect('wishlist')
