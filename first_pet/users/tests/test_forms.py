import pytest
from users.forms import UserRegistrationForm, UserLoginForm, UserProfileForm


@pytest.mark.django_db
def test_registration_form_valid():
    data = {
        'email': 'newuser@example.com',
        'password1': 'newpassword123',
        'password2': 'newpassword123',
    }
    form = UserRegistrationForm(data=data)
    assert form.is_valid()
    user = form.save()
    assert user.email == 'newuser@example.com'


@pytest.mark.django_db
def test_registration_form_invalid_password():
    data = {
        'email': 'newuser@example.com',
        'password1': 'short',
        'password2': 'short',
    }
    form = UserRegistrationForm(data=data)
    assert not form.is_valid()
    assert 'password1' in form.errors


@pytest.mark.django_db
def test_login_form_valid(test_user):
    data = {'email': 'user@test.com', 'password': 'password123'}
    form = UserLoginForm(data=data)
    assert form.is_valid()


@pytest.mark.django_db
def test_login_form_invalid():
    data = {'email': 'wrong@test.com', 'password': 'wrongpassword123'}
    form = UserLoginForm(data=data)
    assert not form.is_valid()


@pytest.mark.django_db
def test_profile_form(test_user):
    data = {
        'first_name': 'Алексей',
        'last_name': 'Сусликов',
        'phone_number': '+375291234567',
        'city': 'Минск',
        'street': 'Зыбицкая',
        'house_number': '3',
        'apartment_number': '2'
    }
    form = UserProfileForm(data=data, instance=test_user)
    assert form.is_valid()
    user = form.save()
    assert user.first_name == 'Алексей'
    assert user.city == 'Минск'