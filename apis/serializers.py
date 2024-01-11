# import serializer from rest_framework
from rest_framework import serializers
 
# import model from models.py
from .models import *
 
# Create a model serializer

class PizzaOrderModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PizzaOrderModel
        fields = ('base','cheese','create_time','customer_name','table_number','order_status','description')