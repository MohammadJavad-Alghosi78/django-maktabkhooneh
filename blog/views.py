from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone
from django.db.models import F
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.
def blog_view(request, **kwargs):
    posts = Post.objects.filter(published_date__lte=timezone.now(), status=1)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name = kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])

    posts = Paginator(posts, 3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    
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

def test(request):
    return render(request, 'test.html')

def blog_category(request, cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name = cat_name)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

