from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from inforratica.views import ComputadorViewSet
from inforratica.views import NotebookViewSet
from inforratica.views import OrdemServicoViewSet
from usuario.views import UsuarioViewSet #, RegistrationViewSet
from uploader.router import router as uploader_router
from usuario.router import router as usuario_router
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r"computadores", ComputadorViewSet)
router.register(r"notebooks", NotebookViewSet)
router.register(r"ordemservico", OrdemServicoViewSet)
router.register(r'usuarios', UsuarioViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api/", include(usuario_router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/media/", include(uploader_router.urls)),
    path('user_info/', OrdemServicoViewSet.as_view({'get': 'user_info'}), name='user-info'),
    path('ordemservico/user_orders/', OrdemServicoViewSet.as_view({'get': 'user_orders'}), name='user-orders'),
]
urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)