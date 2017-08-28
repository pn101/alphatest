from django.http.response import HttpResponse


def home(request):
    return HttpResponse("Hello World")

def mypage(request, name):
    return HttpResponse("Hello " + name)
