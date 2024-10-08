import json
from django.conf import settings
from django.http.response import HttpResponse as HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

with open(settings.REACT_ASSET_MANIFEST) as manifest_file:
    manifest = json.load(manifest_file)

main_js = manifest['files']['main.js'][8:]
main_css = manifest['files']['main.css'][8:]

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'core/index.html'
    login_url = 'login'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
                
        context['react_static_js'] = main_js 
        context['react_static_css'] = main_css

        return context
