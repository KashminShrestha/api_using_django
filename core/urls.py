from django.urls import path
# from .views import category_list, category_detail
# from .views import CategoryDetail, CategoryList
# from .views import CategoryViewSet, ProductViewSet
from rest_framework import routers
from core.views import login, register

router = routers.SimpleRouter()

# using router
urlpatterns = [
    path('login', login),
    path('register', register),

]+router.urls
