from django.utils.deprecation import MiddlewareMixin
from django.core.handlers.wsgi import WSGIRequest
from rest_framework_simplejwt.tokens import AccessToken

class BearerMiddleware(MiddlewareMixin):    
    def process_request(self, request: WSGIRequest):
        if request.user.is_authenticated:
            access = AccessToken.for_user(request.user)
            request.META['HTTP_AUTHORIZATION'] = f"Bearer {access}"