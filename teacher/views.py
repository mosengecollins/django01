from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView
from teacher.models import Teacher

from django.views.generic import DetailView


class TeacherList(ListView):
    model = Teacher




class TeacherDetail(DetailView):
    model = Teacher
    context_object_name = 'teacher'
    queryset = Teacher.objects.all()


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['teacher_list'] = Teacher.objects.all()
        return context
