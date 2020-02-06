from rest_framework import serializers, routers, viewsets
from orders.models import Order, OrderItem


class OrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    buyer = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    first_name = serializers.CharField(required=True, max_length=50)
    last_name = serializers.CharField(required=True, max_length=50)
    email = serializers.EmailField()
    address = serializers.CharField(required=True, max_length=50)
    postal_code = serializers.CharField(required=True, max_length=50)
    city = serializers.CharField(required=True, max_length=50)
    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()
    paid = serializers.BooleanField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Order.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.id = validated_data.get('title', instance.id)
        instance.buyer = validated_data.get('code', instance.buyer)
        instance.first_name = validated_data.get('linenos', instance.first_name)
        instance.last_name = validated_data.get('language', instance.last_name)
        instance.email = validated_data.get('style', instance.email)
        instance.address = validated_data.get('style', instance.address)
        instance.post_code = validated_data.get('style', instance.post_code)
        instance.city = validated_data.get('style', instance.city)
        instance.created = validated_data.get('style', instance.created)
        instance.updated = validated_data.get('style', instance.updated)
        instance.email = validated_data.get('style', instance.email)
        instance.save()
        return instance


# Serializers define the API representation
class OrderItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['order', 'product', 'price', 'quantity', 'is_returned']


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


