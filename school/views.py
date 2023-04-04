from rest_framework import viewsets
from school.models import Student, Course, Registration
from school.serializer import StudentSerializer, CourseSerializer, RegistrationSerializer


class StudentsViewSets(viewsets.ModelViewSet):
    """"Show all students"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CourseViewSets(viewsets.ModelViewSet):
    """Show all courses"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class RegistrationViewSets(viewsets.ModelViewSet):
    """Show all registrations"""
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
