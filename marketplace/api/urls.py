from django.urls import path

from marketplace.api import views

urlpatterns = [
    path('default', views.default_product),
    path('home', views.HomeViewAPI.as_view()),
    path('products', views.ProductListAPIView.as_view()),
    #path('testimonials', views.TestimonialsAPIView.as_view()),
    path('orders', views.OrderListAPIView.as_view()),
    path('orders/<slug:slug>', views.OrderRetrieveAPIView.as_view()),
    path('categories', views.CategoryListAPIView.as_view()),
    path('categories/<int:pk>/products', views.ProductsByCategoryListAPIView.as_view()),
    path('products/<int:pk>', views.ProductRetrieveAPIView.as_view()),
    path('cart', views.CartCreateAPIView.as_view()),
    path('cart/<int:pk>', views.CartListView.as_view())
]
