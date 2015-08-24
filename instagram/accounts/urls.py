from __future__ import absolute_import

from django.conf.urls import url

from . import view


urlpatterns = [
    url(r'^u/signup', view.SignUpView.as_view(), name='signup'),
]
