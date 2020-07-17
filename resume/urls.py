from django.urls import path

from resume.views import resume_index, project_detail

app_name = 'resume'

urlpatterns = [
    path('', resume_index, name='resume_index'),
    path('projects/<slug>/', project_detail, name='project_detail'),
]