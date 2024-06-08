from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .models import Category, Product, File
from .serializers import CategorySerializer, ProductSerializer, FileSerializer


class ProductListView(APIView):

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True, context={'request': request})
        return Response(serializer.data)


# from django.http import JsonResponse
# from django.views import View
# from .models import Product
# from .serializers import ProductSerializer

# class ProductListView(View):
#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return JsonResponse(serializer.data, safe=False)
