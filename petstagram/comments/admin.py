from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('body', 'created_at', 'user')
    list_filter = ('created_at', 'user')
    search_fields = ('body',)
    date_hierarchy = 'created_at'


admin.site.register(Comment, CommentAdmin)
