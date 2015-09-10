from __future__ import absolute_import

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(
        r'^users/$',
        views.ListAccountView.as_view(),
        name='user_list'
    ),
    url(
        r'^(?P<username>[-\w]{5,30})/$',
        views.DetailAccountView.as_view(),
        name='profile'
    ),
    url(
        r'^(?P<username>[-\w]{5,30})/update/$',
        views.UpdateAccountView.as_view(),
        name='update'
    ),
    url(
        r'^(?P<username>[-\w]{5,30})/update/password/$',
        views.ChangePasswordView.as_view(),
        name='change_password'
    ),
    url(
        r'^(?P<username>[-\w]{5,30})/followers$',
        views.FollowersListView.as_view(),
        name='followers'
    ),
    url(
        r'^(?P<username>[-\w]{5,30})/following/$',
        views.FollowingListView.as_view(),
        name='following'
    ),
    url(
        r'^(?P<username>[-\w]{5,30})/follow/$',
        views.follow_view,
        name='follow'
    ),
    url(
        r'^(?P<username>[-\w]{5,30})/unfollow/$',
        views.unfollow_view,
        name='unfollow'
    ),
]
