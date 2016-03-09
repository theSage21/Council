from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from voting import models

def home(request):
    C = {} # context
    template = 'voting/home.html'
    C['topics'] = models.Topic.objects.filter(published=True).order_by('-active')
    return render(request, template, C)

@login_required
def topic(request, tid):
    template = 'voting/topic.html'
    context={'tid': tid}
    context['topic'] = get_object_or_404(models.Topic, pk=tid)
    context['vote_yes'], context['vote_no'] = context['topic'].stats()
    if request.method == 'GET':
        vote = models.Vote.objects.filter(user=request.user,
                                           topic=context['topic']
                                           ).first()
        if vote:
            context['answer'] = 'Yes' if vote.value else 'NO'
        else:
            if context['topic'].active:
                context['form'] = models.VoteForm()
    elif request.method == 'POST':
        if context['topic'].active:
            form = models.VoteForm(request.POST)
            if form.is_valid():
                vote = form.save(commit=False)
                vote.user = request.user
                vote.topic = context['topic']
                vote.save()
            else:
                context['form'] = form
    return render(request, template, context)
