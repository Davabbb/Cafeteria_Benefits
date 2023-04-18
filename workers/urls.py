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
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    #path('', views.home, name='home'),
    path('', views.shop, name='shop'),
    path('user', views.user, name='user'),
    path('purchase/<int:pk>/', views.product_purchase, name='product_purchase'),
    path('wishlist_add/<int:pk>', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist_remove/<int:pk>', views.remove_from_wishlist, name='remove_from_wishlist'),
    # path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', views.login_view, name='login'),

    path('shop', views.shop, name='shop'),
]
