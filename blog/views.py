from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone
from django.db.models import F


# Create your views here.
def blog_view(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    post = get_object_or_404(Post, pk=pid)
    post.counted_view += 1
    post.save()
    context = {'post': post }
    return render(request, 'blog/blog-single.html', context)

def test(request, pid):
    post = get_object_or_404(Post, pk=pid)
    context = {'post': post }
    return render(request, 'test.html', context)