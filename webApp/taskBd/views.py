from pickle import TRUE
from urllib import response
from django.shortcuts import render
from django.template.defaulttags import register
from .models import taskiq
from .forms import taskiqForm
from django.views.generic import DetailView
from django.http import HttpResponseNotFound
from django.http import HttpResponseRedirect

def First(request):
    if 'ask' in request.COOKIES and 'ask_list' in request.COOKIES:
        id_ask=int(request.COOKIES['ask'])
        while 1:
            try:
                test = taskiq.objects.get(id=id_ask+1)
                break
            except taskiq.DoesNotExist:
                id_ask-=1
                if id_ask < 0:
                    return HttpResponseNotFound("<h2>Test not found</h2>")

        response = render(request, 'main/test.html', {'test': test})
        response.set_cookie('ask', id_ask)
        return response
    else:
        test = taskiq.objects.all()
        response = render(request, 'main/test.html', {'test': test[0]})
        response.set_cookie('ask', 0)
        list_answer = "0000000000"
        response.set_cookie('ask_list', list_answer)
        return response

    print(request)
    return render(request, 'main/test.html', {'task1': test[0]})


class СhangingTest (DetailView):
    model = taskiq
    template_name = 'main/test.html'
    context_object_name = 'test'

def test(request, pk):
    test = taskiq.objects.all()
    return render(request, 'main/test.html', {'test': test[pk+1]})


def edit(request, pk):
    try:
        test = taskiq.objects.get(id=pk)
 
        if request.method == "POST":
            test.select = request.POST.get(f"{pk}")
            test.save()
            # return HttpResponseRedirect(f"{pk+1}")
            return render(request, "main/test.html", {"test": test})
        else:
            if 'n' in request.COOKIES:
                response = render(request, "main/test.html", {"test": test})
                response.set_cookie('n', pk)
                return response
            # return render(request, "main/test.html", {"test": test})
            # return HttpResponseRedirect(f"{pk}")
            # next_test = taskiq.objects.all()
            # print(f"{pk}={pk+1}")
    except taskiq.DoesNotExist:
        return HttpResponseNotFound("<h2>Test not found</h2>")
# def test1(request, id):


