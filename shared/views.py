from django.shortcuts import render


def home_page_view(request):
    return render(request, 'shared/home.html')


def contact_page_view(request):
    return render(request, 'shared/contact.html')


def about_page_view(request):
    return render(request, 'shared/about-us.html')