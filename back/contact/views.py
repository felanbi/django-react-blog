from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Contact
from .forms import ContactForm
from django.contrib import messages

class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact/contact.html'
    success_url = reverse_lazy('contact') 

    def form_valid(self, form: ContactForm) -> HttpResponse:
        messages.success(self.request, "OK")
        
        return super().form_valid(form)
    
