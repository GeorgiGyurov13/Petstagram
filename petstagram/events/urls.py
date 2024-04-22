from django.urls import path

from petstagram.events import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('<int:event_id>/', views.event_detail, name='event_detail'),
    path('create/', views.create_event, name='create_event'),
    path('<int:event_id>/like/', views.like_event, name='like_event'),
]
