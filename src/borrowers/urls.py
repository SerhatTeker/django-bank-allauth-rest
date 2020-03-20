from django.urls import path, include

from rest_framework import routers

from .views import index_view, BorrowerViewSet, InvoiceViewSet


router = routers.DefaultRouter()
router.register('borrowers', BorrowerViewSet, base_name='borrowers')
router.register('invoices', InvoiceViewSet, base_name='invoices')


urlpatterns = [
    path('', index_view, name='index'),

    # http://localhost:8000/api/borrowers
    # http://localhost:8000/api/invoices
    path('api/', include(router.urls)),
]
