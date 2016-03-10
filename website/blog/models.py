from django.db import models
from django.core.urlresolvers import reverse


class Post(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=100)
    text = models.TextField(help_text='Enter text in Markdown format')
    published = models.BooleanField(default=False)
    pinned = models.BooleanField(default=False)

    stamp = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('blogpost', args=[self.pk])
