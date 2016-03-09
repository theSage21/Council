from django.contrib import admin
from voting import models

@admin.register(models.Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'active', 'published')


@admin.register(models.Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'topic', 'value')
