from .models import Wishlist

def wishlist_count(request):
    if request.user.is_authenticated:
        return {
            'wishlist_count': Wishlist.objects.filter(user=request.user).count()
        }
    return {}
