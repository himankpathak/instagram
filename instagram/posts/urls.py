from __future__ import absolute_import

from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        r'create/$',
        views.CreatePostView.as_view(),
        name='create'
    ),
    url(
        r'(?P<slug>[\w\-]{10})/$',
        views.DetailPostView.as_view(),
        name='view'
    ),
    url(
        r'(?P<slug>[\w\-]{10})/update/$',
        views.UpdatePostView.as_view(),
        name='update'
    ),
    url(
        r'(?P<slug>[\w\-]{10})/delete/$',
        views.DeletePostView.as_view(),
        name='delete'
    ),
    url(
        r'(?P<slug>[\w\-]{10})/like/$',
        views.like_post_view,
        name='like'
    ),
    url(
        r'(?P<slug>[\w\-]{10})/unlike/$',
        views.unlike_post_view,
        name='unlike'
    ),
]
