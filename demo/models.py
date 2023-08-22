from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=20)
    cover = models.FileField("templates/cover")
    published = models.DateField(default=None, blank=True, null=True)