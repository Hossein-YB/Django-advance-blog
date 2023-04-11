from django.db import models

# Create your models here.


class Blog(models.Model):
    """this is a class define post for blog app"""
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.SET_NULL)
    image = models.ImageField(null=True, blank=True)
    content = models.TextField()
    status = models.BooleanField()
    category = models.ForeignKey('Category', on_delete=models.SET_NULL)

    datetime_create = models.DateTimeField(auto_now_add=True)
    datetime_update = models.DateTimeField(auto_now=True)
    datetime_publish = models.DateTimeField()
    
    def __str__(self) -> str:
        return self.title
    

class Category(models.Model):
    """this is a class for set posts category"""
    name = models.CharField(max_length=1000)
    
    def __str__(self) -> str:
        return self.name