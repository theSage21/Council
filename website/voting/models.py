from django.db import models
from django import forms
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User



class Topic(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=100)
    text = models.TextField()
    active = models.BooleanField(default=False)
    published = models.BooleanField(default=False)

    def stats(self):
        "Yes no Stats for this Topic"
        votes = Vote.objects.filter(topic=self).exclude(value=None)
        yes = votes.filter(value=True).count()
        no = votes.filter(value=False).count()
        return yes, no
    
    def get_absolute_url(self):
        return reverse('topic', args=[self.pk])


class Vote(models.Model):
    def __str__(self):
        return '{} -on- {}'.format(self.user.__str__(),
                                   self.topic.__str__())
    user = models.ForeignKey(User, related_name='user_vote')
    topic = models.ForeignKey(Topic, related_name='topic_vote')
    value = models.NullBooleanField(default=None, verbose_name='Your_vote')

    class Meta:
        unique_together = ('user', 'topic')

class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ('value', )
