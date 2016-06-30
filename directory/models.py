from django.db import models
from django.contrib.auth.models import User
import os.path
from time import strftime

class Year(models.Model):
    pass

class Domain(models.Model):
    name = models.CharField(max_length=80)


# With python 2, these methods must be defined in the main body in order to be serialized by manage.py makemigrations.
def upload_to_photo(instance, filename):
    name, extension = os.path.splitext(filename)
    return str(instance.user.username) + "-photo-" + strftime("%Y_%m_%d-%H_%M_%S") + extension
def upload_to_cv(instance, filename):
    name, extension = os.path.splitext(filename)
    return str(instance.user.username) + "-cv-" + strftime("%Y_%m_%d-%H_%M_%S") + extension


class Alumnus(models.Model):
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    Gender = (
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
    )

    PRIVACY_HIDENAME = 0
    PRIVACY_DISPLAYNAME = 1
    Privacy = (
        (PRIVACY_HIDENAME, 'Hide name in the unauthenticated area'),
        (PRIVACY_DISPLAYNAME, 'Display name in the unauthenticated area'),
    )

    user = models.OneToOneField(User) # Contains (among others) username, first_name, last_name, email, password
    gender = models.IntegerField(choices=Gender)
    photo = models.ImageField(null=True, upload_to=upload_to_photo)
    cv = models.FileField(null=True, upload_to=upload_to_cv)
    year = models.ForeignKey(Year)
    phone1 = models.CharField(max_length=20, null=True)
    phone2 = models.CharField(max_length=20, null=True)
    postal = models.CharField(max_length=160, null=True)
    website = models.URLField(null=True)
    presentation = models.TextField(null=True)
    diploma = models.CharField(max_length=80, null=True)
    company = models.CharField(max_length=160, null=True)
    job = models.CharField(max_length=160, null=True)
    keywords = models.CharField(max_length=1000, null=True)
    domain = models.ForeignKey(Domain, null=True)
    privacy = models.BooleanField(choices=Privacy, default=PRIVACY_DISPLAYNAME)
    last_visit = models.DateTimeField(null=True)
