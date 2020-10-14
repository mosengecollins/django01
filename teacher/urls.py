
from django.urls import path
from teacher.views import TeacherList
from teacher.views import TeacherDetail


urlpatterns = [
    path('teacher/', TeacherList.as_view()),
    path('teacher/<int:pk>/', TeacherDetail.as_view(), name='teacher-detail'),
]



