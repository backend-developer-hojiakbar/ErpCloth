from rest_framework import serializers, exceptions
from .models import Product, Order
from rest_framework.serializers import ModelSerializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    def update(self, instance, validated_data):
        instance.soni = validated_data.get('count')
        print(validated_data.get('count'))
        instance.save()
        return instance


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OmborSoniSerializer(ModelSerializer):
    def validate(self, data):
        if data['productSoni'] < data['soniOrder']:
            raise exceptions.ValidationError(detail="Omborda bu sondan kam mahsulot qolgan")
        return data
    def update(self, instance, validated_data):
        instance.productSoni = validated_data.get('productSoni', instance.productSoni)
        instance.soniOrder = self.context['soniOrder']
        instance.save()
        return instance

    class Meta:
        model = Product
        fields = '__all__'