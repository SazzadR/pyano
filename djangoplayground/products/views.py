from django.shortcuts import render, get_object_or_404

from .models import Product


def products_list_view(request):
    products = Product.objects.all()

    return render(request, 'products/list.html', {
        'products': products
    })


def products_details_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    return render(request, 'products/detail.html', {
        'product': product
    })
