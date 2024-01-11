from django.shortcuts import render
import math
import time
# Create your views here.
# import viewsets
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from django.http import HttpResponse
from django.core import serializers
from django.http import Http404, HttpResponseNotAllowed
# from .models import Restaurant, Dish, Tag
from rest_framework.renderers import JSONRenderer
import json
 
# import local data
from .models import PizzaOrderModel
from .serializers import PizzaOrderModelSerializer
from tasks import update_status_accepted_to_preparing,update_status_preparing_to_dispatched,update_status_dispatched_to_delivered


@csrf_exempt
def place_order(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        print(body)
        for pizza in body['pizza']:
            new_order = PizzaOrderModel(
                base = pizza['base'],
                cheese = pizza['cheese'],
                # toppings = body("toppings"),
                create_time = math.trunc(time.time())  ,
                customer_name = pizza['customer_name'],
                table_number = pizza['table_number'],
                order_status = pizza['order_status'],
                description = pizza['description'],
            )
            new_order.save()
            # print(OrderModel.objects.latest('id'))
            saved_row_id = (PizzaOrderModel.objects.last()).id
            update_status_accepted_to_preparing.apply_async(args=[saved_row_id],countdown = 60)
            update_status_preparing_to_dispatched.apply_async(args=[saved_row_id],countdown = 3*60)
            update_status_dispatched_to_delivered.apply_async(args=[saved_row_id],countdown = 5*60)
        print("Order for {} pizzas placed".format(len(body['pizza'])))
        return HttpResponse(status=200)
    else:
        raise HttpResponseNotAllowed("Method is not supported")

@csrf_exempt
def get_order_status(request):
    if request.method == 'GET':
        try:
            order = PizzaOrderModel.objects.get(id=int(request.GET['order_id']))
            print(order)
        except PizzaOrderModel.DoesNotExist:
            raise Http404("Restaurant does not exist")
        # data = json.loads(order)
        # data = serializers.serialize("json", order)
        serializer = PizzaOrderModelSerializer(order)
        json = JSONRenderer().render(serializer.data)
        return HttpResponse(json)
    else:
        raise HttpResponseNotAllowed("Method is not supported")
