from django.db import models
from django import forms

# Create your models here.

class Player(models.Model):
    PLAYER_ID = models.IntegerField(primary_key=True)
    NAME = models.CharField(max_length=100)
    POSITION = models.CharField(max_length=10)
    CMP = models.FloatField(null=True, blank=True)
    PASS_ATT = models.FloatField(null=True, blank=True)
    PASS_PCT = models.FloatField(null=True, blank=True)
    PASS_YDS = models.FloatField(null=True, blank=True)
    PASS_YPA = models.FloatField(null=True, blank=True)
    PASS_TD = models.FloatField(null=True, blank=True)
    INT = models.FloatField(null=True, blank=True)
    SACKS = models.FloatField(null=True, blank=True)
    RUSH_ATT = models.FloatField(null=True, blank=True)
    RUSH_YDS = models.FloatField(null=True, blank=True)
    RUSH_YPA = models.FloatField(null=True, blank=True)
    RUSH_LG = models.FloatField(null=True, blank=True)
    RUSH_20 = models.FloatField(null=True, blank=True)
    RUSH_TD = models.FloatField(null=True, blank=True)
    REC = models.FloatField(null=True, blank=True)
    TGT = models.FloatField(null=True, blank=True)
    REC_YDS = models.FloatField(null=True, blank=True)
    REC_LG = models.FloatField(null=True, blank=True)
    REC_20 = models.FloatField(null=True, blank=True)
    YPR = models.FloatField(null=True, blank=True)
    REC_TD = models.FloatField(null=True, blank=True)
    FL = models.FloatField(null=True, blank=True)
    G = models.FloatField(null=True, blank=True)
    FPTS_G = models.FloatField(null=True, blank=True)
    OVERALL_PTS = models.FloatField(null=True, blank=True)
    PPR = models.FloatField(null=True, blank=True)
    PPR_G = models.FloatField(null=True, blank=True)

    class Meta: 
        db_table = "player_projections"
        managed = False

    def __str__(self):
        return self.NAME

class FantasyTeam(models.Model): 
    name = models.CharField(max_length=100)
    players = models.ManyToManyField('Player')
