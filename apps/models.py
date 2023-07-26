from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Model


# Create your models here.

class User(AbstractUser):
    image = models.ImageField(upload_to='profile_pics', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField(null=True, blank=True)


class Skill(Model):
    user_id = models.ForeignKey('apps.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    level = models.IntegerField()


class Portfolio(Model):
    user_id = models.ForeignKey('apps.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='portfolio/', blank=True, null=True)
    title = models.TextField()
    type_choose = (
        ('Web Design', 'Web Design'),
        ('Gaming', 'Gaming'),
        ('Programming', 'Programming'),
        ('Graphic Design', 'Graphic Design')
    )
    category = models.CharField(max_length=255, choices=type_choose)
    dis = models.TextField()
    company = models.CharField(max_length=255)
    create_at = models.DateField(auto_now_add=True)


class Blog(Model):
    user_id = models.ForeignKey('apps.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_pics/', blank=True, null=True)
    title = models.CharField(max_length=255)
    dis = models.TextField()


class Experince(Model):
    user_id = models.ForeignKey('apps.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_pics/', blank=True, null=True)
    title = models.CharField(max_length=255)
    dis = models.TextField()
    location = models.CharField(max_length=200, null=True, blank=True)


class Education(Model):
    user_id = models.ForeignKey('apps.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_pics/', blank=True, null=True)
    title = models.CharField(max_length=255)
    dis = models.TextField()


class Comment(Model):
    name = models.CharField(max_length=255)
    author_id = models.ForeignKey('apps.User', on_delete=models.CASCADE)
    post_id = models.ForeignKey('apps.Blog', on_delete=models.CASCADE)
    text = models.TextField()
    email = models.EmailField(max_length=255, null=True, blank=True)
    date = models.DateField(auto_now_add=True)

