import pytest
from django.test import Client
from users.models import User


@pytest.fixture
def test_user():
    user = User.objects.create_user(
        email='user@test.com',
        password='password123',
        first_name='User',
        last_name='Test'
    )
    return user


@pytest.fixture
def test_superuser():
    admin = User.objects.create_superuser(
        email='superuser@test.com',
        password='password12345',
        first_name='Superuser',
        last_name='Test'
    )
    return admin


#неаутентифицированный пользователь
@pytest.fixture
def client():
    return Client()


#аутентифицированный пользователь
@pytest.fixture
def logged_in_client(client, test_user):
    client.login(email='user@test.com', password='password123')
    return client


