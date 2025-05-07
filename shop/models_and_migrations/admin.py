from django.contrib import admin

from .models import GoITeeens, Child


# Register your models here.
@admin.register(GoITeeens, Child)
class Market(admin.ModelAdmin):
    pass