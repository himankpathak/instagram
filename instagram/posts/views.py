from __future__ import absolute_import

from django.views import generic

from braces import views

from .models import Post
from .forms import PostForm


class ViewPostView(
        views.LoginRequiredMixin,
        generic.DetailView
):
    model = Post
    template_name = 'posts/view.html'
    context_object_name = 'post'

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Post.objects.filter(slug=slug)


class CreatePostView(
        views.LoginRequiredMixin,
        generic.CreateView
):
    model = Post
    form_class = PostForm
    template_name = 'posts/form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super(CreatePostView, self).form_valid(form)
