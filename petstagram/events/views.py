from django.shortcuts import render, redirect, get_object_or_404
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


# def like_event(request, event_id):
#     event = get_object_or_404(PetEvent, id=event_id)
#     event.likes += 1
#     event.save()
#     return redirect('event_detail', event_id=event_id)

def like_event(request, event_id):
    event = get_object_or_404(PetEvent, id=event_id)
    session_key = request.session.session_key

    liked_events = request.session.get('liked_events', [])
    if event_id in liked_events:
        event.likes -= 1
        liked_events.remove(event_id)
    else:
        event.likes += 1
        liked_events.append(event_id)

    request.session['liked_events'] = liked_events
    request.session.save()

    event.save()
    return redirect('event_detail', event_id=event_id)