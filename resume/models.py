from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

get_rated_choices = list(zip(range(1, 10 + 1), range(1, 10 + 1)))


class SocialMediaLink(models.Model):
    # social_media = choices
    display_name = models.TextField()
    url = models.URLField()

    small_icon = models.ImageField()
    large_icon = models.ImageField()


class Education(models.Model):
    class Degree(models.TextChoices):
        ASSOCIATE = 'A'
        BACHELOR = 'B'
        MASTER = 'M'
        DOCTORAL = 'D'

    year_start = models.PositiveSmallIntegerField()
    year_end = models.PositiveSmallIntegerField()

    degree = models.CharField(max_length=1, choices=Degree.choices)

    major = models.TextField()
    minor = models.TextField(blank=True, default='')

    school_name_full = models.TextField()
    school_name_acronym = models.CharField(default='', max_length=10)

    description = models.TextField(blank=True, default='')
    gpa = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(4.0)])

    small_icon = models.ImageField()
    large_icon = models.ImageField()


class Skill(models.Model):
    rated_value = models.PositiveSmallIntegerField(choices=get_rated_choices)
    # TODO make a tag
    skill = models.TextField()


class Courses(models.Model):
    course_vendor = models.TextField()
    year_start = models.PositiveSmallIntegerField(help_text="YYYY")
    year_end = models.PositiveSmallIntegerField(help_text="YYYY")

    link = models.URLField()
    description = models.TextField(blank=True, default='')

    small_icon = models.ImageField()
    large_icon = models.ImageField()
