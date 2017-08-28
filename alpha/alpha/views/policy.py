from django.shortcuts import render


def policy(request):
    return render(
        request,
        "policy.html",
        {
            "site_title": "Policy",
            "site_name": "Policy",
        },
    )
