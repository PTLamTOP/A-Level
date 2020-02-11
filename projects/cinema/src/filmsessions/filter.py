from django_filters import DateRangeFilter, DateTimeFilter
import django_filters
from .models import FilmSession


class FilmSessionFilter(django_filters.FilterSet):
    # field_name should be name of Model's field which is used for filter
    start_date = DateTimeFilter(field_name='time_from', lookup_expr='gt', label="From Datetime YY-MM-DD HH:MM")
    end_date = DateTimeFilter(field_name='time_from', lookup_expr='lt', label="To Datetime YY-MM-DD HH:MM")
    date_range = DateRangeFilter(field_name='period', label="Period")

    class Meta:
        model = FilmSession
        fields = ('hall', )

