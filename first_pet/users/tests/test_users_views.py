import pytest
from django.urls import reverse
from users.models import User


@pytest.mark.django_db
def test_register(client):
    url = reverse('users:register')
    data = {
        'email': 'newuser@example.com',
        'password1': 'strongpassword123',
        'password2': 'strongpassword123',
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert User.objects.filter(email='newuser@example.com').exists()


@pytest.mark.django_db
def test_user_login(client, test_user):
    url = reverse('users:user_login')
    data = {'email': 'user@test.com', 'password': 'password123'}
    response = client.post(url, data)
    assert response.status_code == 302


@pytest.mark.django_db
def test_user_logout(logged_in_client):
    url = reverse('users:user_logout')
    response = logged_in_client.get(url)
    assert response.status_code == 302
    assert '/users/login' in response.url


#страница профиля закрыта от анонимных пользователей
@pytest.mark.django_db
def test_profile_requires_login(client):
    url = reverse('users:profile')
    response = client.get(url)
    assert response.status_code == 302
    assert '/users/login' in response.url


#авторизованный пользователь видит страницу профиля
@pytest.mark.django_db
def test_profile_access(logged_in_client):
    url = reverse('users:profile')
    response = logged_in_client.get(url)
    assert response.status_code == 200


