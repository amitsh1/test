# tables.py
import django_tables2 as tables
from .models import Rent
class RentTable(tables.Table):
    class Meta:
        model = Rent