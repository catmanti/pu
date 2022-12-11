# Create your models here.
from django.db import models
from django.urls import reverse


class Insti(models.Model):
    code = models.TextField(db_column='Code', blank=True, null=True)
    institution = models.TextField(
        db_column='Institution', blank=True, null=True)
    type = models.TextField(db_column='Type', blank=True, null=True)
    moharea = models.TextField(db_column='MOHArea', blank=True, null=True)
    pollingdivision = models.TextField(
        db_column='PollingDivision', blank=True, null=True)
    instisinhala = models.TextField(
        db_column='InstiSinhala', blank=True, null=True)
    institutetelno = models.TextField(
        db_column='InstituteTelNo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'insti'

    def __str__(self):
        return str(self.institution)


class PollingDivision(models.Model):
    """Polling Divisions"""
    DISTRICT = [
        ('PU', 'PU'),
        ('KU', 'KU'),
    ]
    name = models.CharField(max_length=30)
    district = models.CharField(max_length=2, choices=DISTRICT)

    def __str__(self):
        return str(self.name)


class MOHArea(models.Model):
    """MOH Areas"""
    DISTRICT = [
        ('PU', 'PU'),
        ('KU', 'KU'),
    ]
    name = models.CharField(max_length=30)
    district = models.CharField(max_length=2, choices=DISTRICT)

    def __str__(self):
        return str(self.name)


class Institution(models.Model):
    """Institution List"""
    TYPES = [
        ('BHA', 'BHA'),
        ('BHB', 'BHB'),
        ('DHA', 'DHA'),
        ('DHB', 'DHB'),
        ('DHC', 'DHC'),
        ('PMCU', 'PMCU'),
        ('UNIT', 'UNIT'),
        ('SDC', 'SDC'),
        ('ADC', 'ADC'),
        ('MOH', 'MOH'),
        ('PGH', 'PGH'),
        ('ELSE', 'ELSE'),
    ]
    DISTRICT = [
        ('PU', 'PU'),
        ('KU', 'KU'),
    ]
    code = models.CharField(blank=True, null=True, max_length=4)
    institution_name = models.CharField(max_length=30)
    type = models.CharField(max_length=4, choices=TYPES)
    district = models.CharField(max_length=2, choices=DISTRICT)
    moh_area = models.ForeignKey(MOHArea, on_delete=models.PROTECT)
    polling_divition = models.ForeignKey(
        PollingDivision, on_delete=models.PROTECT)
    sinhala_name = models.CharField(blank=True, null=True, max_length=30)
    tel_no = models.CharField(blank=True, null=True, max_length=10)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.institution_name)

    def get_absolute_url(self):
        return reverse('insti-detail', kwargs={'pk': self.pk})
