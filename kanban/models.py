from django.db import models

# Create your models here.
class Kanban(models.Model):
    Title = models.CharField(max_length=100)
    Status = models.CharField(max_length=100)
    Priority = models.CharField(max_length=100, blank=True, null=True)
    Summary = models.CharField(max_length=100, blank=True, null=True)
    Type = models.CharField(max_length=100, blank=True, null=True)
    Tags = models.CharField(max_length=100, blank=True, null=True)
    Assignee = models.CharField(max_length=100, blank=True, null=True)
    Color = models.CharField(max_length=100, blank=True, null=True)
    ClassName = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.Title
