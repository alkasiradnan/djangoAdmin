from django.db import models
from reader_definition.models import  ReaderDefinition
from  transformer_definition.models import TransformerDefinition
from writer_definition.models import   WriterDefinition


# Create your models here.

class Configuration(models.Model):
    configurationName = models.CharField(max_length=50)
    reader = models.ForeignKey(ReaderDefinition,on_delete = models.CASCADE)
    transformer = models.ForeignKey(TransformerDefinition,on_delete=models.CASCADE)
    writer = models.ForeignKey(WriterDefinition,on_delete=models.CASCADE,unique=False)
