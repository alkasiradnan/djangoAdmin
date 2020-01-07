from django.db import models

# Create your models here.

class WriterDefinition(models.Model):
	writerName = models.CharField(max_length=50)
	host = models.CharField(max_length=50)
	dbName = models.CharField(max_length=50)
	username =models.CharField(max_length=50)
	password = models.CharField(max_length=50)

	def __str__(self):
		return self.writerName
