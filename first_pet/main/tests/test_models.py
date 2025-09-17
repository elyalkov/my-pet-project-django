import pytest


@pytest.mark.django_db #создает временную тестовую БД
def test_category(category):
    assert str(category) == "Птицы"


@pytest.mark.django_db
def test_category_get_absolute_url(category):
    url = category.get_absolute_url()
    assert "/category/pticy/" in url


@pytest.mark.django_db
def test_product(product):
    assert str(product) == "Попугай"


@pytest.mark.django_db
def test_product_get_absolute_url(product):
    url = product.get_absolute_url()
    assert "/product/popugaj/" in url