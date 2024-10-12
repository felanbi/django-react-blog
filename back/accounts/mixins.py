from django.shortcuts import redirect
from django.contrib.auth.mixins import AccessMixin
from django.http.request import HttpRequest

class RedirectAuthenticatedMixin(AccessMixin):
    def dispatch(self, request: HttpRequest, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        
        return super().dispatch(request, *args, **kwargs)
