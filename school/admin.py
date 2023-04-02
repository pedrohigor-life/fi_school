from django.contrib import admin
from school.models import Student, Course


class Students(admin.ModelAdmin):
    list_display = ('id', 'name', 'rg', 'cpf', 'birth_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20


class Courses(admin.ModelAdmin):
    list_display = ('id', 'course_code', 'description')
    list_display_links = ('id', 'course_code')
    search_fields = ('course_code',)
    list_per_page = 20


admin.site.register(Student, Students)
admin.site.register(Course, Courses)
