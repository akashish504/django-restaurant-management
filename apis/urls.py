# basic URL Configurations
from django.urls import include, path
# import routers
from rest_framework import routers

# import everything from views
from . import views

# define the router
router = routers.DefaultRouter()

# define the router path and viewset to be used
# router.register(r'menuModel', views.MenuModelSet)

# specify URL Path for rest_framework

urlpatterns = [
    path('placeOrder/', views.place_order ),
    path('orderStatus/', views.get_order_status ),
	path('api-auth/', include('rest_framework.urls'))
]
