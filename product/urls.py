from django.urls import path
from .views import (Home,PrdocutDetail)
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('product-details', PrdocutDetail.as_view(), name='product_details'),
]