from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


class UserInline(admin.StackedInline):
    model = Worker
    can_delete = False
    verbose_name_plural = 'Доп. информация'


class UserAdmin(UserAdmin):
    inlines = (UserInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Worker)
