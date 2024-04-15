from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from project.settings import MEDIA_URL, MEDIA_ROOT, STATIC_URL, STATIC_ROOT

urlpatterns = [
    path('documentation/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('api/bookings/', include('bookings.urls')),
    path('api/cart/', include('carts.urls')),
    path('api/orders/', include('orders.urls')),
    path('api/products/', include('products.urls')),
    path('api/user/', include('profiles.urls')),
    path('api/study_areas/', include('study_areas.urls')),
    path('api/buddy/', include('buddy.urls')),
]

urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
