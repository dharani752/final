from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserViewSet, ParagraphViewSet,search,create_user
from rest_framework.authentication import TokenAuthentication
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
# Create a schema view for Swagger documentation
schema_view = get_schema_view(
    openapi.Info(
        title="Your API Title",
        default_version='v1',
        description="Your API description",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,  # Set to False if you want to restrict access
    authentication_classes=(TokenAuthentication,), 
    permission_classes=(permissions.AllowAny,), # Add TokenAuthentication here
)

# Define your API endpoints
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'paragraphs', ParagraphViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('search/<str:word>/', search, name='search'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('documentation/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('create-user/', create_user, name='create-user')
]

