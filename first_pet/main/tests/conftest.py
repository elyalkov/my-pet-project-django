import pytest
from main.models import Category, Product
from django.core.files.uploadedfile import SimpleUploadedFile


@pytest.fixture
def category():
    return Category.objects.create(name="Птицы", slug="pticy")


@pytest.fixture
def product(category):
    image = SimpleUploadedFile(  #временный пустой файл изображения
        name='popugaj.jpg',
        content=b'file_content',
        content_type='image/jpeg'
    )

    return Product.objects.create(
        category=category,
        name="Попугай",
        slug="popugaj",
        image=image,
        description="Маленький попугай",
        price=50,
        available=True,
    )