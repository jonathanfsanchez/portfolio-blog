from django.contrib import admin

from resume.models import SocialMediaLink, Education, Skill, Course, Experience, Project


@admin.register(SocialMediaLink)
class SocialMediaLinkAdmin(admin.ModelAdmin):
    list_display = ('display_name',)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('year_range_str', 'school_name_acronym', 'degree',
                    'major')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('skill', 'rated_value')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('year_start', 'vendor', 'title')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('month_year_range_str', 'company', 'title')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('year_start', 'title')
