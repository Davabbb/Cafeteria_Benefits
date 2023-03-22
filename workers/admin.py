from django.contrib import admin
from .models import *


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


admin.site.register(Worker)

