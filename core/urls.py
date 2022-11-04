from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.shop, name='shop'),
    path('cart/', views.cart, name='cart'),
    path('check-out/', views.checkout, name='check-out'),
    path('product/<str:key>', views.product, name='product'),
    path('category/<slug:slug>', views.category, name='category'),
    path('sub-category/<slug:slug>', views.subCategory, name='sub-category'),
    
]

urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)