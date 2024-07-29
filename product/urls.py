from django.urls import path
# from .views import (Home,PrdocutDetail)
from . import views
urlpatterns = [
    # path('', Home.as_view(), name='home'),
    path('', views.json_to_csv, name='home'),
    # path('product-details', PrdocutDetail.as_view(), name='product_details'),
]