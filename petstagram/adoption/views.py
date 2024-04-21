from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .forms import PetCreationForm
from .models import AdoptablePet


class PetCreateView(CreateView):
    model = AdoptablePet
    form_class = PetCreationForm
    template_name = 'adoption/pet_create.html'
    success_url = reverse_lazy('pet-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class PetListView(ListView):
    model = AdoptablePet
    template_name = 'adoption/pet_list.html'
    context_object_name = 'pets'


def adopt_pet(request):
    if request.method == 'POST':
        # Get the ID of the pet to be adopted from the form data
        pet_id = request.POST.get('pet_id')

        # Retrieve the pet from the database using the ID
        pet = get_object_or_404(AdoptablePet, pk=pet_id)

        # Update the pet's adoption status (assuming you have a boolean field named 'adopted')
        pet.adopted = True
        pet.save()

        return render(request, 'adoption/pet_adopted.html', {'pet': pet})  # Placeholder response
    else:
        return HttpResponse('Method not allowed', status=405)
