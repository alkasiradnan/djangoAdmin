from django.db import models

# Create your models here.

class ReaderDefinition(models.Model):
    LOCAL = 1
    HTTP = 2
    SFTP = 3
    TYPES = (
        (LOCAL, 'LOCAL'),
        (HTTP, 'HTTP'),
        (SFTP, 'SFTP'),
    )
    readerName = models.CharField(max_length=50)
    path = models.CharField(max_length=250)
    type = models.PositiveSmallIntegerField(choices=TYPES, blank=True, null=True)

    def __str__(self):
        return self.readerName
