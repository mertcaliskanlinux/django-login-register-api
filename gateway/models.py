from django.db import models
from user.models import CustomUser
# Create your models here.

class Jwt(models.Model):
    user = models.ForeignKey(CustomUser,related_name="login_user",on_delete=models.CASCADE)
    access = models.TextField()
    refresh = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
