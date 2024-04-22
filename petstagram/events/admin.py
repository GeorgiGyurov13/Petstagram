from django.contrib import admin
from .models import PetEvent

class PetEventAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'location', 'date_time', 'likes')
    list_filter = ('date_time',)
    search_fields = ('name', 'description', 'location')
    date_hierarchy = 'date_time'

admin.site.register(PetEvent, PetEventAdmin)
