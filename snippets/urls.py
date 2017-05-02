from django.conf.urls import url, include
from snippets import views
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

# Create router & register our viewsets w/ it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

schema_view = get_schema_view(title='Pastebin API')

# The API URLs are determined automatically by the router
# Include the login URLs for the browsable API
urlpatterns = [
        url(r'^schema/$', schema_view),
        url(r'^', include(router.urls)),
        url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
