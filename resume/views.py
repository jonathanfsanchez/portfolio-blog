from django.shortcuts import render, get_object_or_404

from resume.models import Project, Skill, Course, Experience, Education


def resume_index(request, template_name='resume/index.html'):
    context = dict()

    context['projects'] = Project.objects.all()
    context['experiences'] = Experience.objects.all()
    context['education'] = Education.objects.all()
    context['skills'] = Skill.objects.all()
    context['courses'] = Course.objects.all()

    return render(request, template_name, context=context)


def project_detail(request, slug, template_name='resume/project.html'):
    context = dict()
    project = get_object_or_404(Project, title_slug=slug)

    context['project'] = project
    return render(request, template_name, context=context)
