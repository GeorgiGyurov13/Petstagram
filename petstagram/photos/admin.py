from django.contrib import admin

from petstagram.photos.models import PetPhoto

from django.contrib import admin
from .models import PetPhoto


class PetPhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo', 'description', 'location', 'created_at', 'modified_at')
    list_filter = ('created_at', 'modified_at')
    search_fields = ('description', 'location')
    date_hierarchy = 'created_at'


admin.site.register(PetPhoto, PetPhotoAdmin)
