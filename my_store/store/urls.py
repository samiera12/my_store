from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('products/',          views.ProductListView.as_view(),       name='product-list'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(),     name='product-detail'),
    path('orders/',            views.OrderListCreateView.as_view(),   name='order-list-create'),
    path('orders/<int:pk>/',   views.OrderDetailView.as_view(),       name='order-detail'),

    path('auth/register/',     views.RegisterView.as_view(),          name='register'),
    path('auth/login/',        TokenObtainPairView.as_view(),         name='token-obtain'),
    path('auth/refresh/',      TokenRefreshView.as_view(),            name='token-refresh'),
    path('auth/profile/',      views.UserProfileView.as_view(),       name='profile'),
]