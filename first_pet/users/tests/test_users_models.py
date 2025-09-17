import pytest


@pytest.mark.django_db
def test_create_user(test_user):
    assert test_user.email == 'user@test.com'
    assert test_user.check_password('password123')
    assert test_user.is_active
    assert not test_user.is_staff


@pytest.mark.django_db
def test_create_superuser(test_superuser):
    assert test_superuser.email == 'superuser@test.com'
    assert test_superuser.is_staff
    assert test_superuser.is_superuser
    assert test_superuser.check_password('password12345')