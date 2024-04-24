from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic as views

from petstagram.photos.forms import PetPhotoCreateForm, PetPhotoEditForm
from petstagram.photos.models import PetPhoto


class PetPhotoCreateView(views.CreateView):
    form_class = PetPhotoCreateForm
    template_name = "photos/create_photo.html"
    queryset = PetPhoto.objects.all() \
        .prefetch_related("pets")

    def get_success_url(self):
        return reverse("details photo", kwargs={
            "pk": self.object.pk,
        })


class PetPhotoDetailView(views.DetailView):
    queryset = PetPhoto.objects.all() \
        .prefetch_related("photolike_set") \
        .prefetch_related("photocomment_set") \
        .prefetch_related("pets")

    template_name = "photos/details_photo.html"


class PetPhotoEditView(views.UpdateView):
    queryset = PetPhoto.objects.all() \
        .prefetch_related("pets")

    template_name = "photos/edit_photo.html"
    form_class = PetPhotoEditForm

    def get_success_url(self):
        return reverse("details photo", kwargs={
            "pk": self.object.pk,
        })


def like_pet_photo(request, pk):
    photo = get_object_or_404(PetPhoto, pk=pk)

    # Toggle like/dislike
    if request.user.is_authenticated:
        if photo.likes_count > 0:
            photo.likes_count -= 1
        else:
            photo.likes_count += 1

        photo.save()

    return JsonResponse({'likes_count': photo.likes_count})