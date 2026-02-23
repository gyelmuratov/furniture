from django.urls import path

from blogs.views import blogs_list_view, blog_detail_view

app_name = 'blogs'

urlpatterns = [
    path('', blogs_list_view, name='list'),
    path('<int:pk>/', blog_detail_view, name='detail')
]