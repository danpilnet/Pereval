from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from pereval_api.views import UserApiView, StatusApiView, PerevalApiView, CoordinatesApiView


router = routers.DefaultRouter()
# router.register(r'submitdata', UserApiView)
router.register(r'submitdata', PerevalApiView)
# router.register(r'submitdata', StatusApiView)
# router.register(r'submitdata', CoordinatesApiView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls))

]
