from django.urls import path
# from .views import category_list, category_detail
# from .views import CategoryDetail, CategoryList
# from .views import CategoryViewSet, ProductViewSet
from rest_framework import routers
from core.views import UserViewSet, activate


router = routers.SimpleRouter()
router.register("user", UserViewSet)

# using router
urlpatterns = [
    path("activation", activate),


]+router.urls
# urlpatterns = [
#     path('login', login),
#     path('register', register),

# ]+router.urls
