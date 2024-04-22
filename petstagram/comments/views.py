from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from .models import Comment
from .forms import CommentForm


def comments_view(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # Create a new comment instance and assign the current user
            comment = form.save(commit=False)
            comment.user = request.user  # Assuming you're using Django's built-in authentication system
            comment.save()
            return redirect('comments_view')
    else:
        form = CommentForm()
    comments = Comment.objects.all()
    return render(request, 'comments/comments.html', {'comments': comments, 'comment_form': form})


