from django.db import models

# Create your models here.



class Topic(models.Model):
    """themes connecting posts with same or simular interests"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string form of the model""" 
        return self.text



class Entry(models.Model):
    """Information contained whithin a certain topics which is theme wise related"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string form of the model""" 
        return f"{self.text[:50]}..."