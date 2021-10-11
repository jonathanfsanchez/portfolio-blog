from django.db import models


class Tag(models.Model):
    displayable_name = models.TextField()
    parent_tag = models.ForeignKey('Tag', null=True, blank=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.displayable_name
