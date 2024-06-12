from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer
from rest_framework import status

# Create your views here.


class CategoryList(APIView):
    def get(self, request):
        if request.method == 'GET':
            categories = Category.objects.all()
            serializer = CategorySerializer(categories, many=True)
            return Response(serializer.data)

    def post(self, request):

        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
# @api_view(['GET', 'POST'])
# def category_list(request):
#     if request.method == 'GET':
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = CategorySerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET'])
# def category_detail(request, pk):
#     try:
#         category = Category.objects.get(pk=pk)
#         serializers = CategorySerializer(category)
#         return Response(serializers.data)
#     except Category.DoesNotExist:
#         return Response(
#             {
#                 'error': 'Category not found',
#             },
#             status=status.HTTP_404_NOT_FOUND,
#         )

@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, pk):
    method = request.method
    category = get_object_or_404(Category, pk=pk)

    if method == "GET":
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    elif method == "PUT":
        serializer = CategorySerializer(category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif method == "DELETE":
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
