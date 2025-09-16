from django.db.models.functions import Lower
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.db.models import Q


def product_list(request, category_slug=None):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    category = None
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    query = request.GET.get('q')
    if query:
        query_lower = query.lower()
        products = products.annotate(
            name_lower=Lower('name'),
            description_lower=Lower('description')
        ).filter(
            Q(name_lower__contains=query_lower) |
            Q(description_lower__contains=query_lower)
        )

    return render(request, 'main/product_list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'query': query})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    cart_product_form = CartAddProductForm()

    return render(request,
                  'main/detail.html',
                  {'product': product,
                            'cart_product_form': cart_product_form})