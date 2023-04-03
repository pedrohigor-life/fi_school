from django.contrib import admin
from django.urls import path, include
from school.views import StudentsViewSets, CourseViewSets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('students', StudentsViewSets, basename='Students')
router.register('courses', CourseViewSets, basename='Courses')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
