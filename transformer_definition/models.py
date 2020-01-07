from django.db import models

# Create your models here.

class TransformerDefinition(models.Model):

    transformerName = models.CharField(max_length=50)
    path = models.CharField(max_length=250)


    def __str__(self):
        return self.transformerName