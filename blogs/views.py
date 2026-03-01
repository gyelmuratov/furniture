from django.shortcuts import render

from blogs.models import Blog,BlogStatus, Category,Tag


def blogs_list_view(request):
    #Category.objects.all()
    cat = Category.objects.get(id=1)
    Category.objects.create(
        title = 'salom'
    )

    context = {
        'blogs': Blog.objects.filter(status=BlogStatus.PUBLISHED),
        'categories': Category.objects.filter(parent = None),
        'tags': Tag.objects.all(),
        'recent_posts': Blog.objects.order_by('-created_at')[:2],
    }

    return render(request, 'blogs/blog-list.html', context)


def blog_detail_view(request, pk):
    try:
        blog = Blog.objects.get(id=pk)
    except Blog.DoesNotExist:
        return render(request, 'shared/404.html')
    context = {
        'blog': blog
    }
    return render(request, 'blogs/blog-detail.html', context)
