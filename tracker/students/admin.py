from django.contrib import admin
from .models import Student, Course, Department, Grade

admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Grade)