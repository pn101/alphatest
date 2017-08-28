from django.http.response import HttpResponse
from django.template import loader


def home(request):
    template = loader.get_template("home.html")
    return HttpResponse(
        template.render(
            {
                "site_name": "Alpha",
            },
            request,
        )
    )

def mypage(request, name):
    return HttpResponse("Hello " + name)
