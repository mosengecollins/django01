from django.contrib import admin

# Register your models here.

from .models import Student, Tel

admin.site.register(Student)
admin.site.register(Tel)
