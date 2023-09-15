from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from bolanarede.views import CamisaViewSet

router = DefaultRouter()
router.register(r"camisas", CamisaViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]