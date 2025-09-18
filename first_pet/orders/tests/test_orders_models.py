import pytest


@pytest.mark.django_db
def test_order_str(order):
    assert str(order) == f"Order {order.id} from Алексей Сусликов"


@pytest.mark.django_db
def test_order_item_str(order_item, product):
    assert str(order_item) == f"2 x {product}"