from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "created_at",
            "updated_at"
        ]
        # fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all()
    )

    price_with_tax = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "price",
            "price_with_tax",
            "category",
            "category_id",
        ]
        # fields = "__all__"

    def get_price_with_tax(self, product: Product):
        return (product.price*0.13)+product.price
