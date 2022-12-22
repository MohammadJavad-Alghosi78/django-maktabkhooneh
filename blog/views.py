from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone
from django.db.models import F


# Create your views here.
def blog_view(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), status=1)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    posts = Post.objects.filter(published_date__lte=timezone.now(), status=1)
    current_post = get_object_or_404(Post, pk=pid, status=1)
    current_post.counted_view += 1
    current_post.save()
    
    prev_post = {}
    next_post = {}
    for post_index in range(len(posts)):
        if(current_post.id == posts[post_index].id):
            if(post_index == 0):
                next_post = posts[post_index + 1]
            elif(post_index == len(posts) - 1):
                prev_post = posts[post_index - 1]
            else:
                next_post = posts[post_index + 1]
                prev_post = posts[post_index - 1]
    
    context = {'post': current_post, 'prev_post': prev_post, 'next_post': next_post }
    return render(request, 'blog/blog-single.html', context)

def test(request, pid):
    post = get_object_or_404(Post, pk=pid)
    context = {'post': post }
    return render(request, 'test.html', context)