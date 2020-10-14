from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from accounts.forms import CustomAccountCreationForm


class SignupPageView(generic.CreateView):
    form_class = CustomAccountCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'