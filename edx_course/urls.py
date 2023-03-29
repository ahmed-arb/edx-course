"""
URLs for edx_course.
"""
from django.urls import path

from edx_course.views import hello


urlpatterns = [
    path(
        'hello/', hello, name='hello'
    ),
]
