from __future__ import absolute_import

from django.views import generic

from braces import views

from .models import Post


class ViewPost(
        views.LoginRequiredMixin,
        generic.DetailView
):
    model = Post
    template_name = 'post/view.html'
    context_object_name = 'post'

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Post.objects.filter(slug=slug)
