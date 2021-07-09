from django_filters import rest_framework as filters
from .models import *


class orderFilter(filters.FilterSet):
    class Meta:
        model = Post
        fields = ['genre', 'language']

    def __init__(self, *args, **kwargs):
        super(orderFilter, self).__init__(*args, **kwargs)
        self.filters['genre'].label = " Filter by Genre"
        self.filters['language'].label = " Filter by Language"


