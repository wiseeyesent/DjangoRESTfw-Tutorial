from django.conf.urls import url, include
from snippets import views
from rest_framework.routers import DefaultRouter

# Create router & register our viewsets w/ it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are determined automatically by the router
# Include the login URLs for the browsable API
urlpatterns = [
        url(r'^', include(router.urls)),
        url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
