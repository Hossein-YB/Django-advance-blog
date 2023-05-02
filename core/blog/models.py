from django.db import models
from django.contrib.auth import get_user_model


# getting user model
user = get_user_model()

class Blog(models.Model):
    """this is a class define post for blog app"""
    title = models.CharField(max_length=100)
    author = models.ForeignKey(user, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(null=True, blank=True)
    content = models.TextField()
    status = models.BooleanField()
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    datetime_publish = models.DateTimeField()
    
    def __str__(self) -> str:
        return self.title
    

class Category(models.Model):
    """this is a class for set posts category"""
    name = models.CharField(max_length=1000)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name