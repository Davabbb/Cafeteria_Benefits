from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)


class PurchaseAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Purchase._meta.fields]

    class Meta:
        model = Purchase


admin.site.register(Purchase, PurchaseAdmin)


class WishlistAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Wishlist._meta.fields]

    class Meta:
        model = Wishlist


admin.site.register(Wishlist, WishlistAdmin)
