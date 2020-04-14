from django.urls import path
from .views import *




urlpatterns = [
    path('', IndexView.as_view()),
    path('shop/', ShopView.as_view(), name='shop')
]
