from django.db import models

class SampleRecord(models.Model):
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title
