from django.shortcuts import render


def blogs_list_view(request):
    return render(request, 'blogs/blog-list.html')

def blog_detail_view(request, pk):
    return render(request, 'blogs/blog-detail.html')
