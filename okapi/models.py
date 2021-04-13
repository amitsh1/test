from django.db import models


class Rent(models.Model):
    PropertyName = models.CharField(max_length=200)
    PropertySqft = models.IntegerField(default=0)
    City = models.CharField(max_length=200)
    LeaseNumber = models.CharField(max_length=200)
    LeaseType = models.CharField(max_length=200)
    TenantName = models.CharField(max_length=200)
    UnitNumber = models.IntegerField(default=0)
    UnitSqft = models.IntegerField(default=0)
    LeaseBeginDate = models.DateTimeField()
    LeaseEndDate = models.DateTimeField()
    AnnualRentSqft= models.FloatField(default=0)
    AnnualRent = models.IntegerField(default=0)


