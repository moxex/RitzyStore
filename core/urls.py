from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from .import views


urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('supersecret/', admin.site.urls),
    path('', views.home, name='home'),
    path('store/', include('store.urls')),
    path('cart/', include('cart.urls')),
    
    path('accounts/', include('accounts.urls')),

    path('orders/', include('orders.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = 'Ritzy Fashion Admin'
admin.site.site_title = 'Ritzy Fashion Admin Portal'
admin.site.index_title = 'Welcome to the Ritzy Fashion Portal'