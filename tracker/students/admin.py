from django.contrib import admin
from .models import Student, Course, Department

admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Course)