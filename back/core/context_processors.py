from django.conf import settings

def env(request):
    return {
        'env': 'DEV' if settings.DEV else ''
    }