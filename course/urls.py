# urls.py
from django.urls import path
from course.views import CourseList
from course.views import CourseDetail


urlpatterns = [
    path('course/', CourseList.as_view()),
#    path('course/<int:pk>', views.CourseDetailView.as_view(), name='course-detail'),
    path('course/<int:pk>/', CourseDetail.as_view(), name='course-detail'),
]
