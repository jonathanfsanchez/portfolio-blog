from django.urls import path

from blog.views import blog_list, blog_view

app_name = 'blog'

urlpatterns = [
    path('', blog_list, name='blog_list'),
    path('<slug>/', blog_view, name='blog_view'),
]
