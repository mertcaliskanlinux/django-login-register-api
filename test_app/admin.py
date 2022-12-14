from django.contrib import admin
from test_app.models import Blog,Car

# Register your models here.
admin.site.register((Blog,Car,))