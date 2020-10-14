from django.contrib import admin

# Register your models here.

from .models import Teacher, TelTeacher

admin.site.register(Teacher)
#@admin.register(Student)
class TeacherAdmin(admin.ModelAdmin):
    pass



admin.site.register(TelTeacher)
