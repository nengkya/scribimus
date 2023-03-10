from django.db import models

from apps.members.models import Member
from core.models import TimeStampedModel


class StoryCategory(models.Model):
    name = models.CharField(max_length=100, blank=False)

    def __unicode__(self):
        return self.name


class Story(TimeStampedModel):
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(default='')
    category = models.ForeignKey(StoryCategory, on_delete=models.CASCADE)
    author = models.ForeignKey(Member, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.title
