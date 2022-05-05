from django.shortcuts import render
from .models import taskiq

def test2(request):
    task1 = taskiq.objects.all()
    print(task1)
    return render(request, 'main/index.html', {'task1:': task1})
