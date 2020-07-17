from django.shortcuts import render, get_object_or_404

# Create your views here.
from resume.models import Project, Skill, Course, Experience


def resume_index(request, template_name='resume/index.html'):
    context = dict()

    projects = Project.objects.all()
    experiences = Experience.objects.all()
    courses = Course.objects.all()
    skills = Skill.objects.all()

    context['projects'] = projects
    context['experiences'] = experiences
    context['courses'] = courses
    context['skills'] = skills
    return render(request, template_name, context=context)


def project_detail(request, slug, template_name='resume/project.html'):
    context = dict()
    project = get_object_or_404(Project, title_slug=slug)

    context['project'] = project
    return render(request, template_name, context=context)
