from django.urls import path
from .views import UserRegisterView, HomeView, LoginView, LogoutView

app_name = "users"

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('panel/', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]