from django.shortcuts import render


def aboutus(request):
    return render(
        request,
        "legal/aboutus.html",
        {
            "site_name": "About Us",
        },
    )


def policy(request):
    return render(
        request,
        "legal/policy.html",
        {
            "site_title": "Policy",
            "site_name": "Policy",
        },
    )


def terms(request):
    return render(
        request,
        "legal/terms.html",
        {
            "site_title": "Terms and Conditions",
            "site_name": "Terms and Conditions",
        },
    )
