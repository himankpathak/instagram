from __future__ import absolute_import

from django.views import generic
from django.contrib.auth.models import User

from .forms import SignUpForm


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    model = User
    template_name = 'accounts/signup.html'
