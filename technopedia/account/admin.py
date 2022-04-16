from django.contrib import admin
from .models import Role, TechUser
# Register your models here.


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['id', 'role_name']


@admin.register(TechUser)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'role_id']
