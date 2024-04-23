from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Feedback

# def submit_feedback(request):
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             helpful = form.cleaned_data['helpful']
#             comment = form.cleaned_data['comment']
#             feedback = Feedback.objects.create(helpful=helpful, comment=comment)
#             # Redirect to the FAQ page after submitting feedback
#             return redirect('all_feedbacks')
#     else:
#         form = FeedbackForm()
#
#     return render(request, 'accounts/submit_feedback.html', {'form': form})
#

from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .models import Feedback


class SubmitFeedbackView(TemplateView):
    template_name = 'accounts/submit_feedback.html'

    def post(self, request, *args, **kwargs):
        helpful = request.POST.get('helpful')
        comment = request.POST.get('comment', '')
        feedback = Feedback.objects.create(helpful=helpful, comment=comment)
        return redirect('all_feedbacks')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        feedbacks = Feedback.objects.all().order_by('-created_at')
        context['feedbacks'] = feedbacks
        return context


def all_feedbacks(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'accounts/all_feedbacks.html', {'feedbacks': feedbacks})
