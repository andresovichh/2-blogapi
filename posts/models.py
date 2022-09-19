from django.conf import settings
from django.db import models
"""
Here, in the models.py file, we create the database
model for each of our blogs.

Each Post, which is our blog entry has a title, a body,
an author, and created and updated times.

We also create a string method for the class
"""
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title