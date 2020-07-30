from django.contrib import admin

from blog.models import Post


@admin.register(Post)
class BlogEntryAdmin(admin.ModelAdmin):
    list_display = ['created', 'updated', 'title_slug', ]
