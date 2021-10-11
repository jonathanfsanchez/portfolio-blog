import tinymce.models
from django.db import models


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    title_slug = models.SlugField()
    title = models.TextField()
    content = tinymce.models.HTMLField()

    tags = models.ManyToManyField('tags.Tag', null=True)

    class Meta:
        ordering = ('-updated',)

    def __str__(self):
        return self.title
