from __future__ import absolute_import

from django.views import generic
from django.core.urlresolvers import reverse_lazy

from braces import views

from .models import Post
from .forms import CreatePostForm, UpdatePostForm, DeletePostForm


class DetailPostView(
        views.LoginRequiredMixin,
        generic.DetailView
):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Post.objects.filter(slug=slug)


class CreatePostView(
        views.LoginRequiredMixin,
        generic.CreateView
):
    model = Post
    form_class = CreatePostForm
    template_name = 'posts/post_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super(CreatePostView, self).form_valid(form)


class UpdatePostView(
        views.LoginRequiredMixin,
        views.FormValidMessageMixin,
        generic.UpdateView
):
    model = Post
    form_valid_message = 'Successfully updated your post.'
    form_class = UpdatePostForm
    template_name = 'posts/post_form.html'


class DeletePostView(
        views.LoginRequiredMixin,
        generic.DeleteView
):
    model = Post
    form_valid_message = 'Successfully deleted your post.'
    form_class = DeletePostForm
    success_url = reverse_lazy('home')
    template_name = 'posts/post_delete.html'
