from django.shortcuts import render


def home(request):
    return render(
        request,
        "home.html",
        {
            "site_name": "Alpha",
        },
    )

def mypage(request, name):
    return HttpResponse("Hello " + name)
