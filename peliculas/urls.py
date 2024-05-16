from rest_framework import routers
from .api import PeliculasViewSet, GenerosViewSet

router = routers.DefaultRouter()

router.register('peliculas', PeliculasViewSet, "peliculas")
router.register('generos', GenerosViewSet, 'generos')

urlpatterns = router.urls
