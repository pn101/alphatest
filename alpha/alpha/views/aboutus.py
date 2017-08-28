from django.shortcuts import render


def aboutus(request):
    return render(
        request,
        "aboutus.html",
        {
            "site_name": "About Us",
        },
    )
