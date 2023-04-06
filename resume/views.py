from django.shortcuts import render, get_object_or_404

from resume.models import Project, Skill, Course, Experience, Education, ResumeOrder
from tags.models import Tag


def resume_index(request, template_name='resume/index.html'):
    context = dict()

    context['section_order'] = []
    resume_order = ResumeOrder.objects.all()
    for section in resume_order:
        section_label = ResumeOrder.Sections(section.section).label
        context['section_order'].append(section_label)

        if section_label == ResumeOrder.Sections.PROJECT.label:
            context['projects'] = Project.objects.all()
        elif section_label == ResumeOrder.Sections.EXPERIENCE.label:
            context['experiences'] = Experience.objects.all()
        elif section_label == ResumeOrder.Sections.EDUCATION.label:
            context['education'] = Education.objects.all()
        elif section_label == ResumeOrder.Sections.SKILLS.label:
            context['skills'] = Skill.objects.all()
        elif section_label == ResumeOrder.Sections.COURSES.label:
            context['courses'] = Course.objects.all()

    return render(request, template_name, context=context)


def project_detail(request, slug, template_name='resume/project.html'):
    context = dict()
    project = get_object_or_404(Project, title_slug=slug)

    context['project'] = project
    return render(request, template_name, context=context)


def tag_search(request, slug, template_name='resume/tags_page.html'):
    context = dict()
    tag = get_object_or_404(Tag, name_slug=slug)

    context['tag'] = tag
    context['section_order'] = []
    resume_order = ResumeOrder.objects.all()
    for section in resume_order:
        section_label = ResumeOrder.Sections(section.section).label
        context['section_order'].append(section_label)

        if section_label == ResumeOrder.Sections.PROJECT.label:
            context['projects'] = Project.objects.filter(tags=tag).all()
        elif section_label == ResumeOrder.Sections.EXPERIENCE.label:
            context['experiences'] = Experience.objects.filter(tags=tag).all()
        elif section_label == ResumeOrder.Sections.EDUCATION.label:
            context['education'] = Education.objects.all()
        elif section_label == ResumeOrder.Sections.SKILLS.label:
            context['skills'] = Skill.objects.filter(tag=tag).all()
        elif section_label == ResumeOrder.Sections.COURSES.label:
            context['courses'] = Course.objects.filter(tags=tag).all()

    return render(request, template_name, context=context)
