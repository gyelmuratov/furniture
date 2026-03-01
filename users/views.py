from django.shortcuts import render

from users.models import UserProfile


def register_view(request):
    if request.method == 'GET':
        return render(request, 'users/register.html')
    else:
        form = UserProfile(request.POST)
        if form.is_valid():
            form.save()
            text = "Successfully registered"