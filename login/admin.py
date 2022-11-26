from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .forms import UserChangeForm, UserCreationForm
from .models import Parque, Senha, User
from django.contrib.auth import admin as auth_admin

@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ("Campos Personalizados", {"fields": ("bio","parque",)}),
    )


admin.site.register(Senha)
admin.site.register(Parque)
