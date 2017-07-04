from django.db import models
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        """Return the Tag title."""
        return self.name


class Activity(models.Model):
    weekdays = (("DOM", "Domingo"),
                ("SEG", "Segunda"),
                ("TER", "Terça"),
                ("QUA", "Quarta"),
                ("QUI", "Quinta"),
                ("SEX", "Sexta"),
                ("SAB", "Sábado"))
    activity_type = models.ManyToManyField(Tag)
    scheduled_day = models.CharField(max_length=200, choices=weekdays,
                                     default="DOM", primary_key=True)
    scheduled_time = models.TimeField(default=timezone.now, primary_key=True)
    end_time = models.TimeField(default=timezone.now, primary_key=True)
    description = models.TextField()
    title = models.CharField(max_length=200)
    local = models.CharField(max_length=200, blank=True)
    status = models.IntegerField()
    is_fixed = models.BooleanField()
    active = models.BooleanField()

    def __str__(self):
        """Return the Activity title."""
        return self.title
