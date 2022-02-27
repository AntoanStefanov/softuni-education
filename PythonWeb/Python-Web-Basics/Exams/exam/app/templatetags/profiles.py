from django import template
from app.models import Profile
register = template.Library()

@register.simple_tag()
def profile():
    return Profile.objects.first()