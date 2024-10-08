from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import views
from django.http import HttpResponse, HttpRequest
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import redirect
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "accounts/register.html"

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        if request.user.is_authenticated:
            return redirect('home')
        
        return super().get(request, *args, **kwargs)

class LoginView(views.LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

    def form_valid(self, form: views.AuthenticationForm) -> HttpResponse:
        response = super().form_valid(form)
        refresh = RefreshToken.for_user(self.request.user)

        response.set_cookie(
            key = 'access',
            value = str(refresh.access_token),
            httponly = True,  
            samesite = 'Lax'
        )

        response.set_cookie(
            key = 'refresh',
            value = str(refresh),
            httponly = True,  
            samesite = 'Lax'
        )

        return response
        