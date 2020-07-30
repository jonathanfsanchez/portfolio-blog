from resume.models import SocialMedia


def social_media(request):
    context = dict()
    context['social_media'] = SocialMedia.objects.all()
    return context
