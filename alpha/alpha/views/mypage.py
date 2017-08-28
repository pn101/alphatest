from django.shortcuts import render


def mypage(request, name):
    return HttpResponse("Hello " + name)
