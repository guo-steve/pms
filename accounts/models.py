from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

"""
User properties:
 - first_name
 - last_name
 - username
 - email
"""

def get_img_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<username><ext>
    return os.path.join(instance.user.username + os.path.splitext(filename)[1])

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    nick_name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to=get_img_path)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birthday = models.DateField(null=True, blank=True)
    mobile = models.CharField(max_length=30, null=True, blank=True)
    designation = models.CharField(max_length=30)
    updated_date = models.DateTimeField(auto_now=True)
