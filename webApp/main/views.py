import re
from django.shortcuts import render
from django.template.defaulttags import register
from taskBd.models import taskiq

def index(request):
    return render(request, 'main/index.html')

# def test(request):
#     task1 = taskiq.objects.all()
#     return render(request, 'main/test.html', {'task1:': task1})

def result(request):
    return render(request, 'main/result.html')

@register.filter
def get_range(value):
    return range(value)
