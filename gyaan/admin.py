from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from gyaan.models import User

class UserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields' : ('name', 'profile_pic', 'description',
                            'role')}),
        )


admin.site.register(User, UserAdmin)
