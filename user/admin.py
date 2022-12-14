from django.contrib import admin
from user.models import CustomUser,CustomUserManager
# Register your models here.
admin.site.register(CustomUser)
# admin.site.register(CustomUserManager)