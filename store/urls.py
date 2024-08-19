from django.urls import path, include
import rest_framework
from rest_framework.routers import DefaultRouter
from .views import OrderItemViewSet, index
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'order_items', OrderItemViewSet)

# urlpatterns = [
#     # path('', include(router.urls)),
#     path('', index, name='index'),
# ]

# store/urls.py

from django.urls import path
from .views import order_items, create_order_items, delete_order_item,index

urlpatterns = [
    path('', index, name='index'),
    path('store/order_items/', order_items, name='order_items'),
    path('store/order_items/create/', create_order_items, name='create_order_items'),
    path('store/order_items/delete/<int:pk>/', delete_order_item, name='delete_order_item'),
]