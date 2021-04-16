from django.db import models

class Concat(models.Aggregate):
    def add_to_query(self, query, alias, col, source, is_summary):
        #we send source=CharField to prevent Django from casting string to int
        aggregate = SQLConcat(col, source=models.CharField(), is_summary=is_summary, **self.extra)
        query.aggregates[alias] = aggregate
        
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


