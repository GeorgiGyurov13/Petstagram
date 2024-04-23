from django.urls import path
from . import views
from .views import SubmitFeedbackView

urlpatterns = [
    path('submit-feedback/', SubmitFeedbackView.as_view(), name='submit_feedback'),
    path('all-feedbacks/', views.all_feedbacks, name='all_feedbacks'),
]
