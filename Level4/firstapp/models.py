#-*- coding: UTF-8 -*-
from django.db import models
from django.contrib.auth.models import User
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

class UserProfile(models.Model):
    belong_to = models.OneToOneField(to=User, related_name="profile")
    phone = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return self.belong_to.username


class Article(models.Model):
    author = models.ForeignKey(to=User, related_name="articles", null=True)
    title = models.CharField(null=True, blank=True, max_length=100)
    content = models.TextField(null=True, blank=True)
    img = models.CharField(null=True, blank=True, max_length=255)
    view_counts = models.IntegerField(default=0)
    like_counts = models.IntegerField(default=0)
    score = models.FloatField(default=1.1)
    is_editor = models.BooleanField(default=False)
    creatime = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
