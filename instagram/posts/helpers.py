from django.db.models import Prefetch

from posts.models import Post, Like
from accounts.models import Connection


def get_posts(user=None, wall=False):
    if not user:
        return None

    users = [user, ]

    if wall:
        users += Connection.objects \
                           .filter(follower=user) \
                           .values_list('following', flat=True)

    return Post.objects \
               .select_related('author') \
               .prefetch_related(
                   Prefetch(
                       'liked_post',
                       queryset=Like.objects.select_related('user'),
                       to_attr='liker'
                   )) \
               .filter(author__in=users) \
               .order_by('date_created')


def get_post(slug=None):
    if not slug:
        return None

    post = Post.objects \
               .select_related('author') \
               .prefetch_related(
                   Prefetch(
                       'liked_post',
                       queryset=Like.objects.select_related('user'),
                       to_attr='liker'
                       )) \
               .get(slug=slug)

    return post
