from django.contrib import admin

from resume.models import SocialMedia, Education, Skill, Course, Experience, Project, ResumeOrder


@admin.register(SocialMedia)
class SocialMediaLinkAdmin(admin.ModelAdmin):
    list_display = ('display_name',)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('year_range_str', 'school_name_acronym', 'degree',
                    'major')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('skill', 'priority')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('year_start', 'vendor', 'title')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('month_year_range_str', 'company', 'title')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('year_start', 'title')


@admin.register(ResumeOrder)
class ResumeOrderAdmin(admin.ModelAdmin):
    list_display = ('priority', 'section')
