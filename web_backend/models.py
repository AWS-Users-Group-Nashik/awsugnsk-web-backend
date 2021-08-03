from django.db import models
from tinymce.models import HTMLField

class Events(models.Model):
    title = models.CharField(max_length=200)
    venue = models.CharField(max_length=200)
    url = models.CharField(max_length=500)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    image_url = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'events'

class Learnings(models.Model):
    title = models.CharField(max_length=200)
    proficiency = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    url = models.CharField(max_length=500)
    image_url = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'learnings'

class Members(models.Model):
    name = models.CharField(max_length=200)
    image_url = models.CharField(max_length=500)
    bio = models.CharField(max_length=1000)
    twitter_url = models.CharField(max_length=300, blank=True, null=True)
    linkedin_url = models.CharField(max_length=300, blank=True, null=True)
    website_url = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    member_type = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'members'

class Stories(models.Model):
    title = models.CharField(max_length=200)
    speaker_name = models.CharField(max_length=200)
    poster_url = models.CharField(max_length=500)
    date = models.DateTimeField()
    content = HTMLField()
    preview_image_url = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'stories'
