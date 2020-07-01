# your django admin
from django.contrib import admin
from user_auth.models import User
from django.contrib.auth.admin import UserAdmin


admin.site.register(User, UserAdmin)
