from rest_framework import serializers

from marketplace.models import Cart, Product, Order, Category, Testimonials, ShippingAddress


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    order = OrderSerializer(many=True)
    category = CategorySerializer
    url = serializers.SerializerMethodField('get_url')
    #album = serializers.SerializerMethodField('get_joined_album')

    class Meta:
        model = Product
        fields = "__all__"

    def get_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.song.url)

    # def get_joined_artist(self, obj):
    #     return ", ".join([a.name for a in obj.album.all()])


class OrderProductSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = "__all__"

class TestimonialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonials
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields ="__all__"


class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = "__all__"
