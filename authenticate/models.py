from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.base_user import BaseUserManager


from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.hashers import make_password
from django.utils import timezone

from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    class Meta:
        verbose_name = u"Usuário"
        verbose_name_plural = u"Usuários"

    CATEGORIA_CHOICES = (
        ('P', u'Professor'),
        ('A', u'Aluno'),
    )

    GENERO_CHOICES = (
        ('M', u'Masculino'),
        ('F', u'Feminino'),
        ('O', u'Outro'),
    )

    username = None
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    categoria = models.CharField(max_length=1, blank=True, null=True, choices=CATEGORIA_CHOICES, verbose_name='Categoria do usuario')
    genero = models.CharField(max_length=1, blank=True, null=True, choices=GENERO_CHOICES, verbose_name='Gênero usuario')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
