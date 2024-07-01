from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UA

# from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

# from core.admin import UserAdmin

User = get_user_model()
# Register your models here.

# admin.site.register(User)
# class User(UserAdmin):
#     pass


@admin.register(User)
class UserAdmin(UA):
    pass

    # search_fields = ["username", "email"]
