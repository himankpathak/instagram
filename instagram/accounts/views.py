from __future__ import absolute_import

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views import generic
from django.core.urlresolvers import reverse_lazy

from braces import views

from .forms import SignUpForm, LoginForm


class ProfileView(
        generic.TemplateView
):
    template_name = 'accounts/profile.html'


class SignUpView(
        views.AnonymousRequiredMixin,
        views.FormValidMessageMixin,
        generic.CreateView
):
    form_class = SignUpForm
    form_valid_message = 'Thanks for signing up, go ahead and login.'
    model = User
    template_name = 'accounts/signup.html'


class LoginView(
        views.AnonymousRequiredMixin,
        views.FormValidMessageMixin,
        generic.FormView
):
    form_class = LoginForm
    form_valid_message = 'You\'re logged in now.'
    success_url = reverse_lazy('home')
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'You\'ve been logged out. Come back soon!')
    return HttpResponseRedirect(reverse_lazy('home'))
