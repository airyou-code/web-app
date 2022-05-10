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
    list_answer = request.COOKIES['ask_list']
    list_corect = "1234561234"
    points = 0
    for i in range(len(list_answer)):
        if list_answer[i] == list_corect[i]:
            points+= 16
    
    response = render(request, 'main/result.html')
    response.delete_cookie('ask')
    response.delete_cookie('ask_list')
    response.set_cookie('result', points)
    return response

@register.filter
def get_range(value):
    return range(value)
