# Generated by Django 3.2 on 2021-04-13 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PropertyName', models.CharField(max_length=200)),
                ('PropertySqft', models.IntegerField(default=0)),
                ('City', models.CharField(max_length=200)),
                ('LeaseNumber', models.CharField(max_length=200)),
                ('LeaseType', models.CharField(max_length=200)),
                ('TenantName', models.CharField(max_length=200)),
                ('UnitNumber', models.IntegerField(default=0)),
                ('UnitSqft', models.IntegerField(default=0)),
                ('LeaseBeginDate', models.DateTimeField()),
                ('LeaseEndDate', models.DateTimeField()),
                ('AnnualRentSqft', models.FloatField(default=0)),
                ('AnnualRent', models.IntegerField(default=0)),
            ],
        ),
    ]
