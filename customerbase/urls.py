from django.contrib import admin
from django.urls import path, include
from django.urls import path
from rest_framework import routers
from core.views import CustomerViewSet, ProfessionViewset, DatasheetViewset, DocumentViewset

router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet, basename="customer")
router.register(r'professions', ProfessionViewset)
router.register(r'datasheets', DatasheetViewset)
router.register(r'documents', DocumentViewset)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/customers/<int:pk>/', CustomerViewSet.as_view({'put': 'update'}), name='customer-detail'),
]
