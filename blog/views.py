from django.shortcuts import render, get_object_or_404

from blog.models import BlogEntry


def blog_list(request, template_name='blog/index.html'):
    context = dict()
    blogs = BlogEntry.objects.all()

    context["blogs"] = blogs
    return render(request, template_name, context=context)


def blog_view(request, slug, template_name='blog/post.html'):
    context = dict()

    blog = get_object_or_404(BlogEntry, url_title=slug)
    context['blog'] = blog

    return render(request, template_name, context=context)
