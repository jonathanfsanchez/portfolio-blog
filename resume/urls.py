from django.urls import path
from resume.views import project_detail, resume_index, tag_search

app_name = 'resume'

urlpatterns = [
    path('', resume_index, name='resume_index'),
    path('projects/<slug>/', project_detail, name='project_detail'),
    path('tags/<slug>/', tag_search, name='tag_search'),
]