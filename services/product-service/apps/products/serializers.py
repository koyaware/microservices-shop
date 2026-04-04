from rest_framework import serializers

from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ["id", "name", "slug", "description", "product_count", "created_at"]

    def get_product_count(self, obj):
        return obj.products.filter(is_active=True).count()


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True)
    is_in_stock = serializers.BooleanField(read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "price",
            "stock_quantity",
            "category",
            "category_name",
            "is_in_stock",
            "stock_quantity",
            "image_url",
            "is_active",
            "is_in_stock",
            "created_at",
            "updated_at",
        ]


class ProductDetailSerializer(ProductSerializer):
    category = CategorySerializer(read_only=True)


class ProductCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "price",
            "stock_quantity",
            "category",
            "image_url",
            "is_active",
        ]
