from django.db import models
from django.conf import settings


AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.user')

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.TimeField(auto_now_add=True, db_index=True)
    category = models.ManyToManyField('blog.Category')
    user = models.ForeignKey(AUTH_USER_MODEL, related_name='added_posts')
    def test(request):
        current_user = request.user
        return current_user

    def __str__(self):
        return '%s' % self.title


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __str__(self):
        return '%s' % self.title


