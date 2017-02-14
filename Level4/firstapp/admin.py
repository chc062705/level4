from django.contrib import admin
from firstapp.models import Article, UserProfile
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Article)
