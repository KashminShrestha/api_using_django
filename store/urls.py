# from django.urls import path
# from .views import category_list, category_detail
# from .views import CategoryDetail, CategoryList
from .views import CategoryViewSet, ProductViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register('categories', CategoryViewSet)
router.register('products', ProductViewSet)

# using router
urlpatterns = [

]+router.urls

# using viewset
""" urlpatterns = [
    path('categories/', CategoryViewSet.as_view(
        {
            'get': 'list',
            'post': 'create',
        }
    )
    ),
    path('categories/<pk>', CategoryViewSet.as_view(
        {
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        }
    )
    ),
] """

# using Classbase api
""" urlpatterns = [
    path('categories/', CategoryList.as_view()),
    path('categories/<pk>', CategoryDetail.as_view()),
] """

# using api view
""" urlpatterns = [
    path('categories/', category_list, name='category-list'),
    path('categories/<pk>', category_detail, name='category-detail'),
] """
