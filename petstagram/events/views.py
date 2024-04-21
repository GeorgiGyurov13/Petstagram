from django.shortcuts import render, redirect
from .models import PetEvent
from .forms import PetEventForm


def event_list(request):
    events = PetEvent.objects.all()
    return render(request, 'events/event_list.html', {'events': events})


def event_detail(request, event_id):
    event = PetEvent.objects.get(id=event_id)
    return render(request, 'events/event_detail.html', {'event': event})


def create_event(request):
    if request.method == 'POST':
        form = PetEventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            return redirect('event_list')
    else:
        form = PetEventForm()
    return render(request, 'events/create_event.html', {'form': form})
