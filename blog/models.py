from django.contrib.auth.models import User
from django.db import models

# Create your models here.






class Tag(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, default='')

    def __str__(self):
        return  self.name

class MyBlog(models.Model):

    title = models.CharField(max_length=100, default='habijabi')
    body = models.TextField()
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(User, null = True)
    timestamp = models.DateTimeField(auto_created='true')
    update = models.DateTimeField(auto_now_add='true')
    # slug = models.SlugField()

    def _str_(self):

        return self.title
