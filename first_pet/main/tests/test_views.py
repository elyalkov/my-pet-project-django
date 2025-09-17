import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_product_list(client, product):
    url = reverse("main:product_list")
    response = client.get(url)
    assert response.status_code == 200
    assert "Попугай" in response.content.decode()


@pytest.mark.django_db
def test_product_list_by_category(client, category, product):
    url = reverse("main:product_list_by_category", args=[category.slug])
    response = client.get(url)
    assert response.status_code == 200
    assert "Попугай" in response.content.decode()


@pytest.mark.django_db
def test_product_search(client, product):
    url = reverse("main:product_list")
    response = client.get(url, {"q": "попугай"})
    assert response.status_code == 200
    assert "Попугай" in response.content.decode()


@pytest.mark.django_db
def test_product_detail(client, product):
    url = reverse("main:product_detail", args=[product.slug])
    response = client.get(url)
    assert response.status_code == 200
    assert "Попугай" in response.content.decode()