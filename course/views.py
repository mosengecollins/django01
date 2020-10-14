from django.shortcuts import render

# Create your views here.

# views.py
from django.views.generic import ListView
from course.models import Course

from django.views.generic import DetailView


class CourseList(ListView):
    model = Course




class CourseDetail(DetailView):
    model = Course
    context_object_name = 'course'
    queryset = Course.objects.all()


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['course_list'] = Course.objects.all()
        return context
