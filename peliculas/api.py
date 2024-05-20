from django.db.models import Q
from rest_framework import viewsets, permissions, filters
from .models import Peliculas, Generos, Directores
from .serializer import PeliculasSerializer, GenerosSerializer, DirectoresSerializer

class PeliculasViewSet(viewsets.ModelViewSet):
  queryset = Peliculas.objects.all()
  serializer_class = PeliculasSerializer
  filter_backends = [filters.SearchFilter]
  search_fields = ["titulo"]
  
  def get_queryset(self):
    queryset = super().get_queryset()
    genero = self.request.query_params.get("genero", None)
    
    if genero:
      queryset = queryset.filter(peliculasgeneros__genero__nombre=genero)
      
    fecha_inicio = self.request.query_params.get("fecha_inicio", None)
    fecha_fin = self.request.query_params.get("fecha_fin", None)
    
    if fecha_inicio and fecha_fin:
      queryset = queryset.filter(
        Q(ano__gte=fecha_inicio) & Q(ano__lte=fecha_fin)
      )
    
    return queryset

class GenerosViewSet(viewsets.ModelViewSet):
  queryset = Generos.objects.all()
  serializer_class = GenerosSerializer

class DirectoresViewSet(viewsets.ModelViewSet):
  queryset = Directores.objects.all()
  serializer_class = DirectoresSerializer