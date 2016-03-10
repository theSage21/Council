from django.shortcuts import render, get_object_or_404
from blog import models


def home(request):
    C = {}  # Context
    template = 'blog/home.html'
    C['posts'] = models.Post.objects.filter(published=True).order_by('-pinned', '-stamp')[:15]
    C['latest'] = models.Post.objects.filter(published=True).order_by('-stamp').first()
    return render(request, template, C)


def blogpost(request, pid):
    C = {} # context
    template = 'blog/post.html'
    C['post'] = get_object_or_404(models.Post, pk=pid)
    if not C['post'].published:
        C['post'] = None
    return render(request, template, C)
