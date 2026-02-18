from django.shortcuts import render


def blogs_list_view(request):
    return render(request, 'blogs/blogs-list.html')