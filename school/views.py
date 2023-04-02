from rest_framework import viewsets
from school.models import Student, Course
from serializer import StudentSerializer, CourseSerializer


class StudentsViewSets(viewsets.ModelViewSet):
    """"Show all students"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CourseViewSets(viewsets.ModelViewSet):
    """Show all courses"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
