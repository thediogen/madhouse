from django.contrib import admin

from .models import Person, Musician, Album, Stuff

# Register your models here.

@admin.register(Person, Musician, Album, Stuff)
class Market(admin.ModelAdmin):
    pass