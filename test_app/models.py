from django.db import models



class Blog(models.Model):
    
    
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.title
    
    

class Car(models.Model):
    
    
    name = models.CharField(max_length=20)
    description = models.TextField()
    author = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name