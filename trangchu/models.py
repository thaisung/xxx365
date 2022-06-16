from django.db import models

# Create your models here.
class cartoon(models.Model):
	title = models.CharField(max_length=255)
	image = models.ImageField()
	# body = models.TextField()
	video = models.FileField(upload_to='', null=True, verbose_name="")

	def __str__(self):
		return self.title
