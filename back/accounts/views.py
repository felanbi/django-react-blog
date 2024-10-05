from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import views
from django.urls import reverse_lazy
from django.views.generic import CreateView

class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "accounts/register.html"

class LoginView(views.LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True