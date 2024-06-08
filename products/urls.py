from django.urls import path
from .views import ProductListView
from rest_framework.views import APIView


urlpatterns = [
    path('products/', ProductListView.as_view()),

]