# from django.shortcuts import get_object_or_404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import mixins, generics
from store.paginations import ProductPagination
from store.filters import ProductFilterSet
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

# from rest_framework import status

from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
)
from .permissions import CustomDjangoModelPermissions

# Create your views here.
# using api view


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

# @api_view(['GET', 'PUT', 'DELETE'])
# def category_detail(request, pk):
#     method = request.method
#     category = get_object_or_404(Category, pk=pk)

#     if method == "GET":
#         serializer = CategorySerializer(category)
#         return Response(serializer.data)
#     elif method == "PUT":
#         serializer = CategorySerializer(category, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif method == "DELETE":
#         category.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# using class base
""" class CategoryList(APIView):
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


class CategoryDetail(APIView):
    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)

        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) """

# using generic
""" class CategoryList(
        generics.GenericAPIView,
        mixins.ListModelMixin,
        mixins.CreateModelMixin
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class CategoryDetail(
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        generics.GenericAPIView
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk) """


# using generic api view
""" class CategoryList(
    generics.ListCreateAPIView
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(
        generics.RetrieveUpdateDestroyAPIView
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer """

# using viewset


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [CustomDjangoModelPermissions]


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.select_related("category").all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    filter_backends = (filters.DjangoFilterBackend, SearchFilter)
    filterset_class = ProductFilterSet
    # filterset_fields = ('category_id',)
    search_fields = ("name",)
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
