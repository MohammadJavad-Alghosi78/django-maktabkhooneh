from django import template
from blog.models import Post

register = template.Library()

@register.inclusion_tag('website/website-latest-posts.html')
def landinglatestposts():
    posts = Post.objects.filter(status=1)[:6]
    print(len(posts))
    return {'posts': posts}

@register.filter
def snippet(value, slice=20):
    return value[:slice] + '...'