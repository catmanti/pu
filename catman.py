# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Insti(models.Model):
    code = models.TextField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    institution = models.TextField(db_column='Institution', blank=True, null=True)  # Field name made lowercase.
    type = models.TextField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    moharea = models.TextField(db_column='MOHArea', blank=True, null=True)  # Field name made lowercase.
    pollingdivision = models.TextField(db_column='PollingDivision', blank=True, null=True)  # Field name made lowercase.
    instisinhala = models.TextField(db_column='InstiSinhala', blank=True, null=True)  # Field name made lowercase.
    institutetelno = models.TextField(db_column='InstituteTelNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'insti'
