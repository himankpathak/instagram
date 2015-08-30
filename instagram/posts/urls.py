from __future__ import absolute_import

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'(?P<slug>[\w\-]{10})/$', views.ViewPost.as_view(), name='post_view'),
]
