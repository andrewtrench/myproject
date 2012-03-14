# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Councilpay(models.Model):
    id = models.IntegerField(primary_key=True)
    role = models.CharField(max_length=354, blank=True)
    note = models.CharField(max_length=9, blank=True)
    number = models.CharField(max_length=9, blank=True)
    salary = models.CharField(max_length=27, blank=True)
    contributions = models.CharField(max_length=27, blank=True)
    allowances = models.CharField(max_length=24, blank=True)
    performance_bonus = models.CharField(max_length=21, blank=True)
    inkind_benefits = models.CharField(max_length=18, blank=True)
    total_package = models.CharField(max_length=27, blank=True)
    province = models.CharField(max_length=39, blank=True)
    council = models.CharField(max_length=96, blank=True)
    class Meta:
        db_table = u'councilpay'

