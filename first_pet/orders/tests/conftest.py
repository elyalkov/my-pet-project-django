import pytest
from django.contrib.auth import get_user_model
from main.models import Category, Product
from orders.models import Order, OrderItem


User = get_user_model()


@pytest.fixture
def user():
    return User.objects.create_user(
        email="newuser@example.com",
        password="password123",
        first_name="Алексей",
        last_name="Сусликов",
        phone_number="+375291234567",
        city="Минск",
        street="Зыбицкая",
        house_number="3",
        apartment_number="2",
    )


@pytest.fixture
def category():
    return Category.objects.create(name="Птицы")


@pytest.fixture
def product(category):
    return Product.objects.create(
        category=category,
        name="Попугай",
        price=100,
    )


@pytest.fixture
def order(user):
    return Order.objects.create(
        user=user,
        first_name="Алексей",
        last_name="Сусликов",
        phone_number="+375291234567",
        city="Минск",
        street="Зыбицкая",
        house_number="3",
        apartment_number="2",
    )


@pytest.fixture
def order_item(order, product):
    return OrderItem.objects.create(
        order=order,
        product_item=product,
        quantity=2,
        total_price=200,
    )