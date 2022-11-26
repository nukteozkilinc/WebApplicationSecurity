from dataclasses import field
from msilib.schema import Class
from random import choices
import django_filters
from .models import Task

class TaskFilter(django_filters.FilterSet):
    CHOICES = (
        ('ascending', 'Ascending'),
        ('descending', 'Descending')
    )


    ordering = django_filters.ChoiceFilter(label ="Ordering", choices=CHOICES, method="filter_by_order")
    class Meta:
        model = Task
        fields = "__all__"
    def filter_by_order(self,queryset, name, value):
        priority ="start_time" if value=="ascending" else '-created'
        return queryset.order_by(priority)


    