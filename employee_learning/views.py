from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, TemplateView
from .models import LearningCourse
from django.urls import reverse_lazy
import datetime

class CourseList(ListView):
    model = LearningCourse
    # queryset = LearningCourse.objects.order_by('-title')
    # queryset = LearningCourse.objects.filter(title__contains='Docker')
    # queryset = LearningCourse.objects.filter(level='B')
    template_name = 'employee_learning/course_list.html'
    context_object_name = 'course_object_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = datetime.date.today()
        return context

class CourseDetail(DetailView):
    model=LearningCourse
    template_name = 'employee_learning/course_detail.html'
    context_object_name = 'course_object'

class CourseCreate(CreateView):
    model=LearningCourse
    template_name = 'employee_learning/course_create.html'
    fields=('title', 'level', 'employee')
    success_url=reverse_lazy ('course_list')

class CourseUpdate(UpdateView):
    model=LearningCourse
    template_name = 'employee_learning/course_update.html'
    fields=('title', 'level','employee')
    success_url=reverse_lazy ('course_list')

class CourseDelete(DeleteView):
    model=LearningCourse
    template_name = 'employee_learning/course_delete.html'
    success_url=reverse_lazy ('course_list')

class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = datetime.date.today()
        return context