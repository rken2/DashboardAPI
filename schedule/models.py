from django.db import models

# Create your models here.
class Schedule(models.Model):
    Subject = models.CharField(max_length=100)
    Location = models.CharField(max_length=100, blank=True, null=True)
    StartTime = models.DateTimeField()
    EndTime = models.DateTimeField()
    IsAllDay = models.BooleanField(default=False)
    Status = models.CharField(max_length=100, blank=True, null=True)
    Priority = models.CharField(max_length=100, blank=True, null=True)
    CategoryColor = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.Subject
