from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from bloodbank.api.viewsets import PatientsViewSet
from doctors.api.viewsets import DoctorsViewSet

router = routers.DefaultRouter()
router.register(r'patients', PatientsViewSet)
router.register(r'doctors', DoctorsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]