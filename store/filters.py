from django_filters import rest_framework as filters
from store.models import Product


class ProductFilterSet(filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            "category": ["exact"],
            "price": ["gte", "lte"],


        }
