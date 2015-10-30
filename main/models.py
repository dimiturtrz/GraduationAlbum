from django.db import models
from django.contrib.auth.models import User

def generate_filename(self, filename):
    url = "files/%s/%s" % (self.user.username, filename)
    return url

class Person(models.Model):
	name = models.CharField(max_length = 50)
	birthday = models.DateField()
	pic = models.FileField(upload_to=generate_filename, blank=True, null=True)
	user = models.ForeignKey(User)
