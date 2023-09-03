from django.contrib import admin
from .models import post, BlogComment

# Register your models here.
admin.site.register((post, BlogComment))
