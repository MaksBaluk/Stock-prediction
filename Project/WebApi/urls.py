from django.urls import path
from .views import *

urlpatterns = [
    path('quote/<slug:symbol>/', get_stocks_info, name='get_stocks_info'),
    path('quote/<slug:symbol>/stocks/', get_stocks_price, name='get_stocks_price'),
    path('quote/<slug:symbol>/stocks/now', get_stocks_price_now, name='get_stocks_price_now'),
]
