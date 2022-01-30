from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
# Create your models here.

class Post(models.Model):
    """Model representing a post"""
    title = models.CharField(max_length=200)
    # Foreign Key used because post can only have one author, but authors can have multiple post
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField(max_length=10000, help_text='Enter the content of your post', default='')
    date_posted = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.title
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('blog:post-detail', kwargs={'pk' : self.pk})


class Comment(models.Model):
    content = models.TextField(max_length=10000)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_published = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    # def get_absolute_url(self):
    #     """Returns the url to access a detail record for this book."""
    #     return reverse('blog:comment-detail', kwargs={'pk' : self.pk})
    
    class Meta:
        ordering = ('-date_published',)

    def __str__(self):
        return f'Comment by {self.author}'