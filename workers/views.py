from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Worker


def home(request):
    user = User.objects.get(username=request.user.username)
    first_name = user.worker.first_name
    last_name = user.worker.last_name
    email_ = user.worker.email
    money = user.worker.money
    data = {"first_name": first_name, "last_name": last_name, "email": email_, "money": money}
    return render(request, "landing/home.html", context=data)


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "landing/signup.html"
