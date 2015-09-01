from __future__ import absolute_import

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.sessions.models import Session
from django.http import HttpResponseRedirect
from django.views import generic
from django.core.urlresolvers import reverse_lazy

from braces import views
from posts.models import Post

from .models import User, Connection
from .forms import AccountForm, LoginForm


class ProfileView(
        views.LoginRequiredMixin,
        generic.DetailView
):
    model = User
    slug_field = 'username'
    slug_url_kwarg = 'username'
    template_name = 'accounts/profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        username = self.kwargs['username']
        context['username'] = username

        session_key = self.request.session.session_key
        session = Session.objects.get(session_key=session_key).get_decoded()
        uid = session.get('_auth_user_id')
        context['user'] = User.objects.get(id=uid)

        context['posts'] = Post.objects.filter(author__username=username)

        context['following'] = Connection.objects.filter(
            follower__username=username).count()
        context['followers'] = Connection.objects.filter(
            following__username=username).count()

        return context


class UpdateAccountView(
        views.LoginRequiredMixin,
        generic.UpdateView
):
    model = User
    slug_field = 'username'
    slug_url_kwarg = 'username'
    form_class = AccountForm
    template_name = 'accounts/account_form.html'


class FollowersListView(
        views.LoginRequiredMixin,
        generic.ListView
):
    model = Connection
    template_name = 'accounts/account_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        username = self.kwargs['username']
        return Connection.objects.filter(following__username=username)

    def get_context_data(self):
        context = super(FollowersListView, self).get_context_data()
        context['mode'] = 'followers'
        return context


class FollowingListView(
        views.LoginRequiredMixin,
        generic.ListView
):
    model = Connection
    template_name = 'accounts/account_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        username = self.kwargs['username']
        return Connection.objects.filter(follower__username=username)

    def get_context_data(self):
        context = super(FollowingListView, self).get_context_data()
        context['mode'] = 'following'
        return context


class SignUpView(
        views.AnonymousRequiredMixin,
        views.FormValidMessageMixin,
        generic.CreateView
):
    form_class = AccountForm
    form_valid_message = 'Thanks for signing up, go ahead and login.'
    model = User
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/account_form.html'


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
