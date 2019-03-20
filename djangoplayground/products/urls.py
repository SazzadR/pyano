from django.urls import path

from . import views

app_name = 'products'
urlpatterns = [
    path('', views.products_list_view, name='list'),
    path('<int:product_id>', views.products_details_view, name='detail'),
]
