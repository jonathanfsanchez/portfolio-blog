from django.shortcuts import render, get_object_or_404

from blog.models import Post


def blog_list(request, template_name='blog/index.html'):
    context = dict()
    blogs = Post.objects.all()

    context["blogs"] = blogs
    return render(request, template_name, context=context)


def blog_view(request, slug, template_name='blog/post.html'):
    context = dict()

    blog = get_object_or_404(Post, title_slug=slug)
    context['blog'] = blog

    return render(request, template_name, context=context)
