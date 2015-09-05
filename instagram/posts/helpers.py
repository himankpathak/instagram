from posts.models import Post, Like


def get_post(username=None):
    posts = Post.objects.filter(author__username=username)

    return {
        post: Like.objects.filter(post=post).count()
        for post in posts
    }
