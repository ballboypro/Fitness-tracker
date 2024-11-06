from django.db import models
from django.contrib.auth.models import AbstractUser

def save_user_img(instance, filename):
	extension = filename.split('.')[-1]
	new_filename = f"{instance.title}'_User'.{extension}"
	return  os.path.join('user_avatar/', new_filename) 

class CustomUser(AbstractUser):
	GENDER_CHOICES = (
	    ('female','FEMALE'),
	    ('male', 'MALE'),
	)
	avatar = models.ImageField(upload_to=save_user_img, blank=True)
	born_date = models.DateField(null=True)
	weight = models.FloatField(null=True)
	height = models.FloatField(null=True)
	gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True)