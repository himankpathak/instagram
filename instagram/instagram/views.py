from django.views import generic

from posts.models import Post


class HomePageView(generic.ListView):
    model = Post
    template_name = 'home.html'
