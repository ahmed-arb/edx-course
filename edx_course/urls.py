"""
URLs for edx_course.
"""
from django.urls import path

from edx_course.views import CourseListAPIView, hello


urlpatterns = [
    path('hello/', hello, name='hello'),
    path('list/', CourseListAPIView.as_view(), name='course_list'),
]
