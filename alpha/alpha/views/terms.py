from django.shortcuts import render


def terms(request):
    return render(
        request,
        "terms.html",
        {
            "site_title": "Terms and Conditions",
            "site_name": "Terms and Conditions",
        },
    )
