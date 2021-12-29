# Here we register our models/tables in the administration.
# adding/controlling tables in administration with one line -> 12
from django.contrib import admin

from django101.models import Person


# https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin
class PersonAdmin(admin.ModelAdmin):
    pass


admin.site.register(Person, PersonAdmin)
