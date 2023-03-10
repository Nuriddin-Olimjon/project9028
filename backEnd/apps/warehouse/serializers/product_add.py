from rest_framework import serializers

from apps.warehouse.models.product import Product


class ProductAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "code",
            "current_arrival_price",
            "current_selling_price",
            "group",
            "brand",
            "description",
            "image",
        )

    def validate_title(self, value):
        exists = Product.objects.filter(is_deleted=False, title=value).exists()
        if exists:
            raise serializers.ValidationError(
                {
                    "key": "title",
                    "error": "already exists"
                }
            )
        return value

    def validate_code(self, value):
        exists = Product.objects.filter(is_deleted=False, code=value).exists()
        if exists:
            raise serializers.ValidationError(
                {
                    "key": "code",
                    "error": "already exists"
                }
            )
        return value
