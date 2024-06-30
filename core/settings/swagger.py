from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import authentication

schema_view = get_schema_view(
    openapi.Info(
        title="Bicycle Rental",
        default_version='v1',
        description="Bicycle Rental API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="timurxboy@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

swagger_urlpatterns = [
    # path('api/docs<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]