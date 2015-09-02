from django.db.models import Q
from django.views import generic

from accounts.models import Connection
from posts.models import Post


class HomePageView(generic.ListView):
    model = Post
    template_name = 'home.html'

    def get_queryset(self):
        following = Connection.objects.filter(
            follower__username=self.request.user
        ).values_list('following').order_by('date_created')

        return Post.objects.filter(
            Q(author__in=following) |
            Q(author__username=self.request.user)
        )
