from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name="index"),
    path('single/<int:pid>', blog_single, name="single"),
    # path('<str:name>/<str:family_name>/<int:age>', test, name="test")
    path('post-<int:pid>', test, name="test")
]