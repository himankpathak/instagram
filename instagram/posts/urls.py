from __future__ import absolute_import

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'(?P<slug>[\w\-]{10})/$', views.ViewPostView.as_view(), name='view'),
    url(r'create/$', views.CreatePostView.as_view(), name='create'),
    url(
        r'(?P<slug>[\w\-]{10})/update/$',
        views.UpdatePostView.as_view(),
        name='update'
    ),
]
