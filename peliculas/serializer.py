from rest_framework import serializers
from .models import Peliculas, Generos, PeliculasGeneros


class GenerosSerializer(serializers.ModelSerializer):
  class Meta:
    model = Generos
    fields = ("id", "nombre")

class PeliculasSerializer(serializers.ModelSerializer):
  generos = serializers.SerializerMethodField()

  class Meta:
    model = Peliculas
    depth = 1
    fields = ("id", "titulo", "ano", "sinopsis", "duracion", "director", "estudio", "generos")

  def get_generos(self, obj):
    generos = PeliculasGeneros.objects.filter(pelicula_id=obj).values_list('genero', flat=True)
    return GenerosSerializer(Generos.objects.filter(id__in=generos), many=True).data