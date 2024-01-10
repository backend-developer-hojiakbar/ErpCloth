from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Product, Order, Category
from .serializers import ProductSerializer, OrderSerializer
from rest_framework.response import Response
from rest_framework import status
class ProductList(APIView):

    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404
class OrderList(APIView):
    def get(self, request, format=None):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            clothID = request.data.get('maxsulotId')
            soniOrder = request.data.get('soni')
            cloth = Product.objects.get(id=clothID)
            serializer_data = ProductSerializer(cloth).data
            soni = serializer_data.get('soni')
            k = soni - soniOrder
            productYangilanganSoni = {
                "count": k
            }
            ProductSerializer.update(self, instance=cloth, validated_data=productYangilanganSoni)
            print("serializer_data ", serializer_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
class SortByCategory(APIView):
    def update(self, request, pk):
        try:
            cloth = Product.objects.get(id=pk)
            serializer_data = ProductSerializer(cloth).data

            data = {
                "status": "Succesful",
                "cloth": serializer_data
            }
            return Response(data)
        except Exception:
            return Response(
                {"status": "Does not exists",
                 "message": "Cloth is not found"}, status=status.HTTP_404_NOT_FOUND
            )
class FromID(APIView):
    def get(self, request, pk):
        try:
            products = Product.objects.all().filter(category_id=pk)
            serializer_data = ProductSerializer(products, many=True).data

            data = {
                "status": "Succesful",
                "products": serializer_data
            }
            return Response(data)
        except Exception:
            return Response(
                {"status": "Does not exists",
                 "message": "Products is not found"}, status=status.HTTP_404_NOT_FOUND
            )
class FromCode(APIView):
    def get(self, request, code):
        try:
            products = Product.objects.all().filter(code__icontains=code)
            serializer_data = ProductSerializer(products, many=True).data

            data = {
                "status": "Succesful",
                "products": serializer_data
            }
            return Response(data)
        except Exception:
            return Response(
                {"status": "Does not exists",
                 "message": "Bunday codeli mahsulot yo'q"}, status=status.HTTP_404_NOT_FOUND
            )
class FromSana(APIView):
    def get(self, request, kun):
        try:
            products = Product.objects.all().filter(code__icontains=code)
            serializer_data = ProductSerializer(products, many=True).data

            data = {
                "status": "Succesful",
                "products": serializer_data
            }
            return Response(data)
        except Exception:
            return Response(
                {"status": "Does not exists",
                 "message": "Bunday codeli mahsulot yo'q"}, status=status.HTTP_404_NOT_FOUND
            )
