from rest_framework import routers
from .api import PeliculasViewSet, GenerosViewSet, DirectoresViewSet

router = routers.DefaultRouter()

router.register('peliculas', PeliculasViewSet, "peliculas")
router.register('generos', GenerosViewSet, 'generos')
router.register('directores', DirectoresViewSet, 'directores')

urlpatterns = router.urls
