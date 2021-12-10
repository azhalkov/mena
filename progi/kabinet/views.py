from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import StatusForm


def form_status(request):
    form = StatusForm()
    return render(request, 'kabinet/status_form.html', {'form': form})


def post_new(request):
    if request.method == "POST":
        form = StatusForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/')
    else:
        form = StatusForm()
    return render(request, 'kabinet/status_form.html', {'form': form})
