from django.db import models

# Create your models here.
class Schedule(models.Model):
    Subject = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    StartTime = models.DateTimeField()
    EndTime = models.DateTimeField()
    IsAllDay = models.BooleanField(default=False)
    Status = models.CharField(max_length=100)
    Priority = models.CharField(max_length=100)
    CategoryColor = models.CharField(max_length=100)

    def __str__(self):
        return self.Subject
