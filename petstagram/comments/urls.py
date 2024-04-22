from django.urls import path
from .views import comments_view

urlpatterns = [
    path('', comments_view, name='comments_view'),
]
