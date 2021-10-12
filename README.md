# Portfolio and Blog

A Django based personal site to showcase your technical portfolio with blogging capability.

Homepage is displayed in a resume format. Skills are ranked based on proficiency. 
Add icons to all your projects, experience, courses, and social media. Tag capability is a WIP.

You can use the admin panel to manage your Blogs, Education, Experience, Courses, Projects, Skills, and Social Media.

## Dependencies
`pip install django`

`pip install django-tinymce`

`pip install Pillow`

## Building
`python manage.py makemigrations tags blog resume`

`python manage.py migrate`

`python manage.py createsuperuser`

`python manage.py runserver`

## Demo
- [Homepage](https://jonathanfsanchez.com)
- [Admin Panel](https://jonathanfsanchez.com/admin)
- User: `demo` Password: `6r3vKEd1eZK%`