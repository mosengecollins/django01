from django.contrib import admin

# Register your models here.

from .models import Course

from .models import Category

admin.site.register(Course)

admin.site.register(Category)
