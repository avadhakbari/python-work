from django.urls import path
from. import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('product_sub_category_details/', views.product_sub_category_details, name='product_sub_category_details'),
    path('add_product_sub_category/', views.add_product_sub_category, name='add_product_sub_category'),
    path('view_product_sub_category/<int:pk>/', views.view_product_sub_category, name='view_product_sub_category'),
    path('update_product_sub_category/<int:pk>/', views.update_product_sub_category, name='update_product_sub_category'),
    path('search_product/', views.search_product, name='search_product'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)