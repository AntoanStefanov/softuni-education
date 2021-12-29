# Here we register our models/tables in the administration(panel).
# adding/controlling tables in administration with one line -> 13
from django.contrib import admin

from django101.cities.models import Person


# https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin
class PersonAdmin(admin.ModelAdmin):
    pass


admin.site.register(Person, PersonAdmin)
