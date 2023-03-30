"""
views for edx_course.
"""
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from lms.djangoapps.course_api.serializers import CourseSerializer

@api_view(['GET'])
def hello(request):
    return Response({'msg': "hello"})

class CourseListAPIView(ListAPIView):

    queryset = CourseOverview.get_all_courses()
    serializer = CourseSerializer
