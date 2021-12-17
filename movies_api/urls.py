"""movies_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
# from film.api.urls import film_router
# from django.urls.conf import include
from film.api.views_mix import FilmCreateListView, FilmUpdateDeleteView
from movies_api.settings import MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions, routers

from film.api.urls import film_router
from country.api.urls import country_router


router = routers.DefaultRouter()
router.registry.extend(film_router.registry)
router.registry.extend(country_router.registry)


urlpatterns = [
    path('api/', include(router.urls)),  # viewset crud
    # path('api/mixin_film/', FilmCreateListView.as_view(), name='Film'),
    # path('api/mixin_film/<int:id>/', FilmUpdateDeleteView.as_view(), name='Film'),
    path('admin/', admin.site.urls),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)


schema_view = get_schema_view(
    openapi.Info(
        title="Movies API",
        default_version='v1',
        url='localhost:8000',
        description="Movies api",
        terms_of_service="",
        contact=openapi.Contact(email="www.librain@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = urlpatterns + [
    path(r'api/swagger/', schema_view.with_ui('swagger',
         cache_timeout=5), name='schema-swagger-ui'),
    path(r'api/redoc/', schema_view.with_ui('redoc',
         cache_timeout=5), name='schema-redoc-ui'),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
