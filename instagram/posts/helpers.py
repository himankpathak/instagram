from posts.models import Post, Like


def get_posts(username=None):
    if not username:
        return None

    posts = Post.objects.filter(author__username=username)

    return {
        post: Like.objects.filter(post=post).count()
        for post in posts
    }


def get_post(slug=None):
    if not slug:
        return None

    post = Post.objects.get(slug=slug)
    likes = Like.objects.filter(post__slug=slug).count()

    return post, likes
