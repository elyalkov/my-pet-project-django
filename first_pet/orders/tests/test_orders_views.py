import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_order_create_get(client, user):
    client.login(email="newuser@example.com", password="password123")
    url = reverse("orders:order_create")
    response = client.get(url)
    assert response.status_code == 200
    assert "form" in response.context


@pytest.mark.django_db
def test_order_create_post(client, user, product):
    client.login(username="newuser@example.com", password="password123")

    url = reverse("orders:order_create")
    data = {
        "first_name": "Алексей",
        "last_name": "Сусликов",
        "phone_number": "+375291234567",
        "city": "Минск",
        "street": "Зыбицкая",
        "house_number": "3",
        "apartment_number": "2",
    }

    response = client.post(url, data)
    #Stripe может вернуть редирект (303)
    assert response.status_code in [200, 303]