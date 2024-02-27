from django.urls import path

from .import views

app_name = 'ishop'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('shop/create/', views.ShopCreateView.as_view(), name='shop_create'),
    path('shop/<int:pk>/', views.ShopDetailView.as_view(), name='shop_detail'),
]
