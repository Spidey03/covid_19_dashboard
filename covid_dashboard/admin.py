# your django admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from covid_dashboard.models\
    import User, Stats, Mandal, District, State
# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Stats)
admin.site.register(Mandal)
admin.site.register(District)
admin.site.register(State)