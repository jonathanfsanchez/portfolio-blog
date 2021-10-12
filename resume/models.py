import tinymce.models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class SocialMedia(models.Model):
    display_name = models.TextField()
    url = models.URLField()

    small_icon = models.ImageField(blank=True, null=True, default=None)

    def __str__(self):
        return self.display_name


class Education(models.Model):
    year_start = models.PositiveSmallIntegerField()
    year_end = models.PositiveSmallIntegerField()

    degree = models.TextField(help_text="e.g. Associates of Arts, or AA")

    major = models.TextField()
    minor = models.TextField(blank=True, default='')

    school_name_full = models.TextField()
    school_name_acronym = models.CharField(default='', max_length=10)

    description = models.TextField(blank=True, default='')
    gpa = models.FloatField(blank=True, null=True, default=None,
                            validators=[MinValueValidator(0.0), MaxValueValidator(4.0)])

    small_icon = models.ImageField(blank=True, null=True, default=None)

    class Meta:
        ordering = ('-year_start',)

    def year_range_str(self):
        return "{start} - {end}".format(start=self.year_start,
                                        end=self.year_end if self.year_end else "Present")

    year_range_str.short_description = "Dates"  # This is so the admin page has correct column header

    def __str__(self):
        return "{years} : {school} - {major}".format(years=self.year_range_str(),
                                                     school=self.school_name_acronym,
                                                     major=self.major)


class Skill(models.Model):
    tag = models.OneToOneField('tags.Tag', on_delete=models.CASCADE)
    priority = models.PositiveSmallIntegerField()

    # displayable in the SECTIONS area. not related to any reference from anywhere else.
    displayable = models.BooleanField(default=True)

    class Meta:
        ordering = ('priority', 'tag')

    def __str__(self):
        return self.tag.displayable_name


class Course(models.Model):
    vendor = models.TextField()

    year_start = models.PositiveSmallIntegerField(help_text="YYYY")
    year_end = models.PositiveSmallIntegerField(help_text="YYYY", blank=True, null=True, default=None)

    is_expiration = models.BooleanField()

    title = models.TextField()
    description = tinymce.models.HTMLField(blank=True)
    link = models.URLField(blank=True, null=True, default=None)

    small_icon = models.ImageField(blank=True, null=True, default=None)

    tags = models.ManyToManyField('tags.Tag', null=True)

    class Meta:
        ordering = ('-year_start',)

    def year_range_str(self):
        if self.is_expiration:
            return "{} - {}".format(self.year_start, self.year_end)
        else:
            return self.year_start

    def __str__(self):
        return "{year} {vendor} - {title}".format(year=self.year_start,
                                                  vendor=self.vendor,
                                                  title=self.title)


class Experience(models.Model):
    company = models.TextField()
    company_small_logo = models.ImageField(blank=True, null=True, default=None)
    company_link = models.URLField(blank=True, null=True, default=None)

    month_start = models.PositiveSmallIntegerField()
    year_start = models.PositiveSmallIntegerField()

    is_current_job = models.BooleanField(default=False)

    month_end = models.PositiveSmallIntegerField(blank=True, null=True, default=None)
    year_end = models.PositiveSmallIntegerField(blank=True, null=True, default=None)

    title = models.TextField()
    description = tinymce.models.HTMLField()
    location = models.TextField()

    tags = models.ManyToManyField('tags.Tag', null=True)

    class Meta:
        ordering = ('-year_start',)

    def month_year_range_str(self):
        range = "{month_start:0>2d}/{year_start} - ".format(month_start=self.month_start,
                                                            year_start=self.year_start)
        if self.is_current_job:
            range += "Present"
        else:
            range += "{month_end:0>2d}/{year_end}".format(month_end=self.month_end,
                                                          year_end=self.year_end)

        return range

    month_year_range_str.short_description = "Dates"  # This is so the admin page has correct column header

    def __str__(self):
        return "{range} | {company} | {title}".format(
            range=self.month_year_range_str(),
            company=self.company,
            title=self.title
        )


class Project(models.Model):
    year_start = models.PositiveSmallIntegerField()
    year_end = models.PositiveSmallIntegerField(blank=True, null=True, default=None)
    is_wip = models.BooleanField()

    git_url = models.URLField(blank=True, null=True, default=None)
    title = models.TextField()
    title_slug = models.SlugField()

    # This is the full project page content
    full_content = tinymce.models.HTMLField()

    # This is the condensed version for the resume page
    resume_content = tinymce.models.HTMLField()

    project_logo = models.ImageField(blank=True, null=True, default=None)

    tags = models.ManyToManyField('tags.Tag', null=True)

    class Meta:
        ordering = ('-year_start',)

    def __str__(self):
        return "{year} - {title}".format(year=self.year_start, title=self.title)

    def get_date_range_str(self):
        range = "{year_start} - ".format(year_start=self.year_start)

        if self.is_wip:
            range += "Present"
        else:
            range += "{year_end}".format(year_end=self.year_end)

        return range


class ResumeOrder(models.Model):
    class Sections(models.TextChoices):
        PROJECT = 'PR', _('Projects')
        EXPERIENCE = 'EX', _('Experience')
        EDUCATION = 'ED', _('Education')
        SKILLS = 'SK', _('Skills')
        COURSES = 'CO', _('Courses')

    section = models.CharField(max_length=2, choices=Sections.choices, unique=True)
    priority = models.PositiveSmallIntegerField(unique=True)

    class Meta:
        ordering = ('priority', 'section',)
