from django.db import models

# Create your models here.


# Main game models

from django.db import models

# Base class user
class User(models.Model):
    user_id = models.IntegerField(max_length=16)
    user_name = models.CharField(max_length=64)
    join_date = models.DateTimeField('date joined')


# Class for matches - match history and such
# include datetime, match result, players, etc.
class Match(models.Model):
    match_id = None
