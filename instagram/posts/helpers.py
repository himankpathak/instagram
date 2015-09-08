from django.db.models import Prefetch

from posts.models import Post, Like
from accounts.models import Connection, User


def get_posts(username=None, wall=False):
    if not username:
        return None

    users = [User.objects.get(username=username), ]

    if wall:
        users += Connection.objects \
                           .filter(follower__username=username) \
                           .values_list('following', flat=True)

    posts = Post.objects \
                .select_related('author') \
                .prefetch_related(
                    Prefetch(
                        'liked_post',
                        queryset=Like.objects.select_related('user'),
                        to_attr='liker'
                    )) \
                .filter(author__in=users) \
                .order_by('date_created')

    for post in posts:
        post.liker = [liker.user for liker in post.liker]

    return posts


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

    post.liker = [liker.user for liker in post.liker]

    return post
