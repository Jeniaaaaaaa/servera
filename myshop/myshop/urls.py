from django.urls import include, re_path, path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^accounts/', include('django.contrib.auth.urls')),
    re_path(r'^cart/', include('cart.urls'), name='cart'),
    re_path(r'^orders/', include('orders.urls', namespace='orders')),
    re_path(r'^', include('shop.urls', namespace='shop')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# from django.urls import include, re_path, path
# from django.contrib import admin
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     re_path(r'^accounts/', include("users.urls")),
#     re_path(r'^accounts/', include('django.contrib.auth.urls')),
#     re_path(r'^admin/', admin.site.urls),
#     re_path(r'^cart/', include('cart.urls'), name='cart'),
#     re_path(r'^orders/', include('orders.urls'), name='orders'),
#     re_path(r'^', include('shop.urls'),name='shop'),
# ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
