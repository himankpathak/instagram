from django.db.models import Q
from django.views import generic
from django.shortcuts import render_to_response
from django.template import RequestContext

from accounts.models import Connection
from posts.models import Post, Like


class HomePageView(generic.ListView):
    model = Post
    template_name = 'home.html'

    def get_queryset(self):
        following = Connection.objects.filter(
            follower__username=self.request.user
        ).values_list('following').order_by('date_created')

        posts = Post.objects.filter(
            Q(author__in=following) |
            Q(author__username=self.request.user)
        )

        return {
            post: Like.objects.filter(post=post).count()
            for post in posts
        }


def handler404(request):
    response = render_to_response(
        '404.html', {},
        context_instance=RequestContext(request)
    )
    response.status_code = 404
    return response
