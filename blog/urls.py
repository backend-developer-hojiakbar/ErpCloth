from .views import ProductList, OrderList, SortByCategory, \
    FromID, FromCode
from django.urls import path
urlpatterns = [
    path('products/', ProductList.as_view()),
    path('orders/', OrderList.as_view()),
    path('SortByCategory/<int:pk>', SortByCategory.as_view(),),
    path('id/<int:pk>', FromID.as_view()),
    path('fromCode/<int:code>', FromCode.as_view()),
]
