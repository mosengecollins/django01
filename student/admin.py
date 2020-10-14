from django.contrib import admin

# Register your models here.

from .models import Student, Tel

admin.site.register(Student)
#@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass



admin.site.register(Tel)
