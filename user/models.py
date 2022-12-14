from django.db import models

from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager


class CustomUserManager(BaseUserManager):
    
    def _create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError("Email fields is required, Email zorunlu alandır !!*")
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user        


    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('name',"admin")
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser is Staff == True")
        
        
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser is_superuser == True")
        
        return self._create_user(email,password,**extra_fields)

class CustomUser(AbstractBaseUser,PermissionsMixin):
    
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False,)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    USERNAME_FIELD = "email"
    object = CustomUserManager()
    
    def __str__(self):
        return self.email