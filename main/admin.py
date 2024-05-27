from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import UserProfile, CustomUser

User = get_user_model()

# Перевірка чи модель User зареєстрована
try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass

class UserProfileInline(admin.StackedInline):
    model = UserProfile

class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    inlines = [UserProfileInline]

# Реєстрація CustomUser з кастомним адміністратором
admin.site.register(CustomUser, CustomUserAdmin)
