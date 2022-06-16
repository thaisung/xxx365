from django.db import models

# Create your models here.
class account(models.Model):
	username1 = models.CharField(max_length=25)
	password1 = models.CharField(max_length=25)
	def __str__(self):
		return self.username1