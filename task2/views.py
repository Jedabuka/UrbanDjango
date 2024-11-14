from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def task_2(request):
    return render(request, 'func_template.html')

class Task2(TemplateView):
    template_name = 'class_template.html'

