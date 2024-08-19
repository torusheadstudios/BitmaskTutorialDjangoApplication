from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import OrderItem
from .serializers import OrderItemSerializer
from .bitmask import ClothingBitMask

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

def index(request):
    context = {
        'colors': ClothingBitMask.export_colors(),
        'sizes': ClothingBitMask.export_sizes(),
        'materials': ClothingBitMask.export_materials()
    }
    return render(request, 'store/index.html', context)

@api_view(['GET'])
def order_items(request):
    order_items = OrderItem.objects.all()
    data = [
        {
            "id": order_item.id,
            "order_name": order_item.order_name,
            "product": order_item.product,
            "quantity": order_item.quantity,
            "bitmask": order_item.bitmask,
        }
        for order_item in order_items
    ]
    return JsonResponse(data, safe=False)

@api_view(['DELETE'])
def delete_order_item(request, pk):
    try:
        order_item = get_object_or_404(OrderItem, pk=pk)
        order_item.delete()
        return Response({"message": "Order item deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_order_items(request):
    try:
        order_name = request.data['order_name']
        items = request.data['items']
        for item in items:
            product = item['product']
            bitmask = item['bitmask']
            quantity = 1  # Assuming each entry in items array is for one product, adjust if needed
            OrderItem.objects.create(order_name=order_name, product=product, bitmask=bitmask, quantity=quantity)
        return Response({"message": "Order items created successfully"}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)