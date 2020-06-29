import tinymce.models
from django.db import models


class BlogEntry(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    url_title = models.SlugField()
    title = models.TextField()
    content = tinymce.models.HTMLField()

    # TODO: tags
    # tags = tagulous.models.TagField(to=SiteWideTags)
