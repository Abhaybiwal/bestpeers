from .models import Cart

def cart_count(request):
    return {
        'cart_count': Cart.objects.count()
    }
