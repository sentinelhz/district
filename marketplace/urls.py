from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = "marketplace"

urlpatterns = [
    path('', index, name='index'),
    path('about_us', about_us, name="about_us"),
    path('cart', cart, name="cart"),
    path('contact', contact, name="contact"),
    path('team',team, name="team"),
    path('order', OrderListView.as_view(), name='albums'),
    path('order/<slug:slug>', OrderDetailView.as_view(), name='order'),
    path('categories', CategoryListView.as_view(), name='category'),
    #path('affirmations/<song_id>', affirmations, name='affirmations'),
    path('categories/<int:pk>', ProductsByCategoryListAPIView.as_view(), name='songs-by-genre'),
    path('products/', include([
        path('make-favorite', favoriteunfavorite, name='product-favorite'),
        path('upload', ProductUploadView.as_view(), name='upload'),
        path('<slug:product_id>', ProductDetailsView.as_view(), name='upload-details'),

    ])),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
