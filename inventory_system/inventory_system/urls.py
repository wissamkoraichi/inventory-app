from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from inventory import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'inventory', views.InventoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
