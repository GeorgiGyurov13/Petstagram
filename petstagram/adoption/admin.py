from django.contrib import admin
from .models import AdoptablePet


class AdoptablePetAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'adoption_status')
    list_filter = ('age', 'gender', 'adoption_status')
    search_fields = ('name', 'description', 'contact_email')
    readonly_fields = ('photo',)  # Assuming photo is a URLField


admin.site.register(AdoptablePet, AdoptablePetAdmin)
