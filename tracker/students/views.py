from urllib import request
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Student, Course, Department, Grade
from django.urls import reverse_lazy


class StudentListView(ListView):
    model = Student
    tempalte_name = 'students/student_list.html'
    context_object_name = 'students'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/student_detail.html'
    context_object_name = 'students'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student = self.get_object()
        context['grades'] = Grade.objects.filter(student=student)
        context['department'] = self.object.department

        return context

class StudentCreateView(CreateView):
    model = Student
    fields = '__all__'
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('student-list')

class StudentUpdateView(UpdateView):
    model = Student
    fields = '__all__'
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('student-list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/student_confirm_delete.html'
    success_url = reverse_lazy('student-list')



