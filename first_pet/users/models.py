from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
#AbstractBaseUser — базовый класс для создания своей кастомной модели пользователя (без username)
#BaseUserManager — менеджер, который управляет созданием пользователей
#PermissionsMixin — добавляет поддержку прав (например, is_superuser, groups, permissions)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields): #**extra_fields — дополнительные поля (имя, город и т.д.)
        if not email:
            raise ValueError('The email field must be set')
        email = self.normalize_email(email) #normalize_email приводит email к "нормальному" виду (например, Test@Email.com → test@email.com)
        user = self.model(email=email, **extra_fields)
        user.set_password(password) #set_password хэширует пароль
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True) #доступ к админке
        extra_fields.setdefault('is_superuser', True) #все права
        return self.create_user(email, password, **extra_fields) #используем функцию для юзера, но с параметрами супера


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=30, blank=True)
    street = models.CharField(max_length=30, blank=True)
    house_number = models.CharField(max_length=10, blank=True)
    apartment_number = models.CharField(max_length=10, blank=True)
    is_active = models.BooleanField(default=True) #служебное поля для входа в систему
    is_staff = models.BooleanField(default=False) #доступ к Django-админке

    USERNAME_FIELD = 'email' #Django по умолчанию логинит по username (используем email вместо username)
    REQUIRED_FIELDS = [] #список обязательных полей при создании суперпользователя (email уже обязателен по умолчанию)

    objects = UserManager()

    def __str__(self):
        return self.email