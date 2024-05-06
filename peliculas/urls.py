from rest_framework import routers
from .api import PeliculasViewSet

router = routers.DefaultRouter()

router.register('peliculas', PeliculasViewSet, "peliculas")

urlpatterns = router.urls
