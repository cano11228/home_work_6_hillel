from django.contrib import admin
from main.models import UserProfile
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


User = get_user_model()


class UserProfileInline(admin.StackedInline):
    model = UserProfile


class UserCastomAdmin(UserAdmin):
    inlines = [UserProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserCastomAdmin)

