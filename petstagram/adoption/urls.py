from django.urls import path
from .views import PetCreateView, PetListView, adopt_pet

urlpatterns = [
    path('pet-create/', PetCreateView.as_view(), name='pet-create'),
    path('pet-list/', PetListView.as_view(), name='pet-list'),
    path('adopt-pet/', adopt_pet, name='adopt-pet'),
]
