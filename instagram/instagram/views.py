from django.views import generic
from django.shortcuts import render_to_response
from django.template import RequestContext

from posts.models import Post
from posts.helpers import get_posts


class HomePageView(generic.ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return get_posts(self.request.user, wall=True)


def handler404(request):
    response = render_to_response(
        '404.html', {},
        context_instance=RequestContext(request)
    )
    response.status_code = 404
    return response
