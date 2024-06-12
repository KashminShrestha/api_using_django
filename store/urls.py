from django.urls import path
from .views import CategoryList, category_detail

urlpatterns = [
    path('categories/', CategoryList.as_view()),
    # path('categories/', category_list, name='category-list'),
    path('categories/<pk>', category_detail, name='category-detail'),
]
