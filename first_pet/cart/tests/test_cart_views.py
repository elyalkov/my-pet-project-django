import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_cart_add(client, product):
    url = reverse('cart:cart_add', args=[product.id])
    response = client.post(url, {'quantity': 2, 'override': False})

    assert response.status_code == 302

    session = client.session  #Проверяем содержимое сессии
    cart = session.get('cart')
    assert cart is not None
    assert str(product.id) in cart
    assert cart[str(product.id)]['quantity'] == 2


@pytest.mark.django_db
def test_cart_remove(client, product):
    session = client.session
    session['cart'] = {str(product.id): {'quantity': 1, 'price': str(product.price)}}
    session.save()

    url = reverse('cart:cart_remove', args=[product.id])
    response = client.post(url)
    assert response.status_code == 302
    session = client.session
    assert str(product.id) not in session.get('cart', {})


@pytest.mark.django_db
def test_cart_detail(client, product):
    url_add = reverse('cart:cart_add', args=[product.id]) #Инициализируем корзину через Cart, чтобы формы создались
    client.post(url_add, {'quantity': 3, 'override': False})

    url = reverse('cart:cart_detail')
    response = client.get(url)
    assert response.status_code == 200
    content = response.content.decode()
    assert "Попугай" in content
    assert 'type="number"' in content