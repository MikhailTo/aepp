# tutorial/tables.py
import django_tables2 as tables
from .models import Speed

class SpeedTable(tables.Table):
    class Meta:
        model = Speed
        fields = ("roll", "task", "cspd", "tspd", "bmav", "bemf", "amav", "aemf", "corr", )
        row_attrs = {
            "data-id": lambda record: record.pk
        }