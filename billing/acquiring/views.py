from django.shortcuts import render
from cart.forms import CartAddProductForm

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Product
#def product_list(request, category_slug=None):

 #   products = Product.objects.filter(available=True)
    
#    return render(request, 'acquiring/product/list.html',
  #      {'products': products})

#def product_detail(request, id, slug):
  #  product = get_object_or_404(Product, id=id, slug=slug, available=True)
 #   cart_product_form = CartAddProductForm()
  #  return render(request, 'acquiring/product/detail.html', {'product': product, 'cart_product_form': cart_product_form})
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'acquiring/product/detail.html', {'product': product, 'cart_product_form': cart_product_form})
