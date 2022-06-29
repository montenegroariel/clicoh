import datetime
import json

from django.db import IntegrityError
from django.db.models import F
from products.models import Product
from rest_framework import serializers, status
from rest_framework.response import Response

from .models import Order, OrderDetail


class OrderDetailSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = OrderDetail
        fields = ['id','cuantity', 'product']



class OrderSerializer(serializers.ModelSerializer):
    order_details = OrderDetailSerializer(many=True, required=False)

    class Meta:
        model = Order
        fields = ['pk','date_time','order_details','get_total','get_total_usd']

    def create(self, validated_data):

        orders_data = validated_data.pop('order_details')
        order = Order.objects.create(**validated_data)
        for order_data in orders_data:
            Product.objects.filter(pk=order_data['product'].id).update(stock = F('stock') - order_data['cuantity'])
            detail = OrderDetail.objects.create(order=order, **order_data)
        return order
    
    def update(self, instance, validated_data):
        new_order_details = validated_data.get('order_details')
        old_order_details = OrderDetail.objects.filter(order=instance)

        for old_od in old_order_details:
            Product.objects.filter(pk=old_od.product.id).update(stock = F('stock') + old_od.cuantity)
            OrderDetail.delete(old_od)

        for new_od in new_order_details:
            OrderDetail.objects.create(**new_od, order=instance)
            Product.objects.filter(pk=new_od['product'].id).update(stock = F('stock') - new_od['cuantity'])
        return instance



    def validate(self,data):
        a=[]
        for detail in data['order_details']:
            product = Product.objects.get(pk=detail['product'].id)
            if product.stock <= 0:
                raise serializers.ValidationError({"product": "The stock of the product must be greater than 0"})
            if detail['product'] in a:
                raise serializers.ValidationError({"product": "the product must be unique in an order"})
            else:
                a.append(detail['product'])
        return data
