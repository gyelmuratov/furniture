import threading

from django.contrib import messages
from django.contrib.auth import get_user_model, login
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.encoding import force_str, force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from users.forms import CustomUserCreationForm, CustomAuthenticationForm
from users.utils import email_verification_token

User = get_user_model()


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()

            # Build verification link
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = email_verification_token.make_token(user)

            link = request.build_absolute_uri(
                reverse('users:verify-email', kwargs={'uidb64': uid, 'token': token})
            )

            # Send email
            thread = threading.Thread(target=send_mail, kwargs={
                'subject': 'Verify your email',
                'message': f'Click to verify your account: {link}',
                'from_email': 'noreply@yourapp.com',
                'recipient_list': [user.email],
            })
            thread.start()

            text = "We sent a confirmation link to your email, please verify it"
            messages.success(request, text)
            return redirect('users:register')
        else:
            errors = []
            for field, field_errors in form.errors.items():
                for error in field_errors:
                    errors.append(f"{field}: {error}")

            error_text = " | ".join(errors)
            messages.error(request, error_text)
            return render(request, 'users/register.html')
    else:
        return render(request, 'users/register.html')


def verify_email_view(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, User.DoesNotExist):
        user = None

    if user and email_verification_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('shared:home')
    else:
        messages.error(request, "Something went wrong, please try again later")
        return render(request, 'users/login.html')


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            login(request, user)
            return redirect('shared:home')
        else:
            errors = []
            for field, field_errors in form.errors.items():
                for error in field_errors:
                    errors.append(f"{field}: {error}")

            error_text = " | ".join(errors)
            messages.error(request, error_text)
            return render(request, 'users/login.html', )
    else:
        return render(request, 'users/login.html', )


def account_view(request):
    return render(request, 'users/account.html')


def reset_password_view(request):
    return render(request, 'users/reset-password.html')