from django.shortcuts import render
from django.views.generic import (
    View,
    CreateView,
    TemplateView
)
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import FormView
# Form
from .forms import UserRegisterForm, UserLoginForm

#models
from .models import User


class HomeView(TemplateView):
    template_name = 'users/home.html'

class LoginView(FormView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    success_url = '/panel'

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        return super(LoginView, self).form_valid(form)
class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class =  UserRegisterForm
    success_url = '/'

    def form_valid(self, form):
        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            genre=form.cleaned_data['genre'],
        )

        return super(UserRegisterView, self).form_valid(form)

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse('users:login')
        )