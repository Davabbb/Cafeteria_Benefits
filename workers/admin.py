from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


# class WorkerInOrderInline(admin.TabularInline):
#     model = WorkerInOrder
#     extra = 0
#
#
# class OrderAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Order._meta.fields]
#     inlines = [ProductInOrderInline]
#
#     class Meta:
#         model = Order

#TEST
class UserInline(admin.StackedInline):
    model = Worker
    can_delete = False
    verbose_name_plural = 'Доп. информация'


class UserAdmin(UserAdmin):
    inlines = (UserInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
#TEST

admin.site.register(Worker)

