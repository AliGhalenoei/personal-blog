from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# Add skills
class Skill(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='icons/')

    def __str__(self) -> str:
        return self.name
    
# add sample work
class SampleWork(models.Model):
    address = models.URLField()
    name = models.CharField(max_length=255,null=True , blank=True)

    def __str__(self) -> str:
        return self.address


class Notification(models.Model):
    """
        When a new blog is created, it notifies people via email. 
    """
    email = models.EmailField(max_length=255 , unique=True)

    def __str__(self) -> str:
        return self.email
    


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    
class Blog(models.Model):

    STATUS_BLOG = [
        ('complete','complete'),
        ('draft','draft')
    ]

    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='user_blog')
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='image_blogs/')
    tags = models.ManyToManyField(Tag , related_name='tags')
    status = models.CharField(max_length=8 , choices=STATUS_BLOG , default='draft')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title





