from django.db import models
import tinymce.models

from resume.models import SocialMediaLink


class Project(models.Model):
    year_start = models.PositiveSmallIntegerField()
    year_end = models.PositiveSmallIntegerField()

    social_media_url = models.OneToOneField(SocialMediaLink,
                                            blank=True, null=True, default=None, on_delete=models.SET_NULL)
    git_url = models.URLField()

    full_content = tinymce.models.HTMLField()
    resume_content = models.TextField()

    # TODO add tagging
    tags = models.TextField()

    def add_tag(self, new_tag):
        self.tags = self.tags + " " + new_tag

    def get_tags(self):
        return self.tags.split()
