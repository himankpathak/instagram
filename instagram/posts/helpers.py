from django.db.models import Count

from posts.models import Post
from accounts.models import User, Connection


def get_posts(username=None, wall=False):
    if not username:
        return None

    users = [User.objects.get(username=username), ]

    if wall:
        users += Connection.objects.filter(
            follower__username=username
        ).values_list('following')

    return Post.objects \
               .annotate(likes=Count('like_post')) \
               .filter(author__in=users) \
               .order_by('date_created')


def get_post(slug=None):
    if not slug:
        return None

    return Post.objects \
               .annotate(likes=Count('like_post')) \
               .get(slug=slug)
