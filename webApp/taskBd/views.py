from django.shortcuts import render
from django.template.defaulttags import register
from .models import taskiq
from .forms import taskiqForm
from django.views.generic import DetailView
from django.http import HttpResponseNotFound

def First(request):
    task1 = taskiq.objects.all()
    print(request)
    return render(request, 'main/test.html', {'task1': task1[0]})


class СhangingTest (DetailView):
    model = taskiq
    template_name = 'main/test.html'
    context_object_name = 'test'

def test(request, pk):
    test = taskiq.objects.all()
    return render(request, 'main/test.html', {'test': test[pk+1]})

# def test1(request, id):


