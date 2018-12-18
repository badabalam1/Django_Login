#from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import CreateUserForm


class CreateUserView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('create_user_done')


class ResisteredView(TemplateView):
    template_name = 'registration/signup_done.html'


class UserLoginView(TemplateView):
    template_name = 'registration/login.html'
