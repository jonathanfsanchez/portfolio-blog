from django.contrib import admin

from resume.models import SocialMediaLink, Education, Skill, Courses

admin.site.register(SocialMediaLink)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Courses)