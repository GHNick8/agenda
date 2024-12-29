from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    datum = models.DateField(blank=True, null=True)
    tijdstip_begin = models.TimeField(blank=True, null=True)
    tijdstip_eind = models.TimeField(blank=True, null=True)
    omschrijving = models.TextField()
    kosten = models.DecimalField(max_digits=7, decimal_places=2)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
    