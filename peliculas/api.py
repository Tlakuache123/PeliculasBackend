from .models import Peliculas
from rest_framework import viewsets, permissions
from .serializer import PeliculasSerializer

class PeliculasViewSet(viewsets.ModelViewSet):
  queryset = Peliculas.objects.all()
  permission_classes = [permissions.AllowAny]
  serializer_class = PeliculasSerializer