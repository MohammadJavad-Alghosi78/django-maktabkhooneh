from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
class Post(models.Model):
    image = models.ImageField(upload_to='blog/', default='default.jpg')
    # models.CASCADE => remove post after remove User
    # models.set_NULL => null post author field(not remove post) after remove user
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    # tag
    category = models.ManyToManyField(Category)
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_date']
        # verbose_name = 'پست' # change name in admin panel
        # verbose_name_plural = 'پست‌ها' # change name in admin panel with 's

    def __str__(self) -> str:
        return "{}".format(self.title)

