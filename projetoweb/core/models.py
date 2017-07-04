from django.db import models
from django.utils import timezone
# Create your models here.

class Tag(models.Model):
	name = models.CharField(max_length=200)


class Activity(models.Model):
	activity_type = models.OneToOneField(Tag,primary_key=True)
	scheduled_datetime = models.DateTimeField(default=timezone.now)
	end_datetime = models.DateTimeField(default=timezone.now)
	description = models.TextField()
	title = models.CharField(max_length=200)
	local = models.CharField(max_length=200, blank=True)
	status = models.IntegerField()
	is_fixed = models.BooleanField()