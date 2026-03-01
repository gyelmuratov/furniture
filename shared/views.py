from django.contrib import messages
from django.shortcuts import render

from shared.forms import ContactForm


def home_page_view(request):
    return render(request, 'shared/home.html')


def contact_page_view(request):
    if request.method == "GET":
        return render(request, 'shared/contact.html')
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            text = "Successfully sent to the admin, thanks for your attention."
            messages.success(request, text)
        else:
            errors = []
            for field, field_errors in form.errors.items():
                for error in field_errors:
                    errors.append(f"{field}: {error}")

            error_text = " | ".join(errors)
            messages.error(request, error_text)
        return render(request, 'shared/contact.html')


def about_page_view(request):
    return render(request, 'shared/about-us.html')