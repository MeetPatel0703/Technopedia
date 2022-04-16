from django.db import models
from generic.models import BaseField
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

# Create your models here.


class Role(BaseField):
    role_name = models.CharField(max_length=70, unique=True)

    class Meta:
        db_table = "role_technopedia"


class TechUser(AbstractUser):
    role = models.ForeignKey(
        Role, on_delete=models.SET_NULL, null=True, default=2)

    # class AbstractUser(AbstractBaseUser, PermissionsMixin):
    #     abstract = True
    # def __str__(self):
    #     return str(self.id)

    class Meta:
        db_table = "user_technopedia"
