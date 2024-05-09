"""Django_aboba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.info, name='info'),
    path('', views.shop, name='shop'),
    path('home', views.shop, name='home'),
    path('home_edit', views.shop_edit, name='home_edit'),
    path('user', views.user, name='user'),
    path('staff', views.staff, name='staff'),
    path('purchase/<int:pk>/', views.product_purchase, name='product_purchase'),
    path('wishlist_add/<int:pk>', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist_remove/<int:pk>', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('receipt/add/', views.receipt_add, name='receipt_add'),
    path('create_worker', views.create_worker, name='create_worker'),
    path('delete_worker', views.delete_worker, name='delete_worker'),
    path('edit_worker', views.edit_worker, name='edit_worker'),
    path('create_product', views.create_product, name='create_product'),
    path('edit_product', views.edit_product, name='edit_product'),
    path('delete_product/<int:pk>', views.delete_product, name='delete_product'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('shop', views.shop, name='shop'),
    path('cart', views.cart, name='cart'),
    path('report/', views.report, name='report'),
    path('info', views.info, name='info'),
    path('export/', views.export_benefits_xls, name='export_benefits_xls')
]
