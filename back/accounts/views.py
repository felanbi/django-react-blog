from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import views
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .mixins import RedirectAuthenticatedMixin

class RegisterView(RedirectAuthenticatedMixin, CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "accounts/register.html"

class LoginView(views.LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('articles')
    redirect_authenticated_user = True

    def form_valid(self, form: views.AuthenticationForm) -> HttpResponse:
        from rest_framework_simplejwt.tokens import RefreshToken

        response = super().form_valid(form)
        refresh = RefreshToken.for_user(self.request.user)

        response.set_cookie('refresh', str(refresh), httponly=True)
        response.set_cookie('access', str(refresh.access_token), httponly=True)

        return response
    
class LogoutView(views.LogoutView):
    def get_default_redirect_url(self) -> str:
        return reverse_lazy('articles')