from django.urls import path, include

from petstagram.photos import views
from petstagram.photos.views import PetPhotoCreateView, PetPhotoEditView, PetPhotoDetailView, like_pet_photo

urlpatterns = (
    path("create/", PetPhotoCreateView.as_view(), name="create photo"),
    path(
        "<int:pk>/",
        include([
            path("", PetPhotoDetailView.as_view(), name="details photo"),
            path("edit/", PetPhotoEditView.as_view(), name="edit photo"),
        ]),
    ),
    path('like/<int:pk>/', like_pet_photo, name='like_pet_photo'),
)
