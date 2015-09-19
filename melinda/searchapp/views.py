from django.shortcuts import render

from rest_framework import viewsets

from .models import Nomenclature, Textmap
from .serializers import NomenclatureSerializer, TextmapSerializer 


class NomenclatureViewSet(viewsets.ModelViewSet):
    queryset = Nomenclature.objects.all()
    serializer_class = NomenclatureSerializer

class TextMapViewSet(viewsets.ModelViewSet):
    queryset = Textmap.objects.all()
    serializer_class = TextmapSerializer


def index(request):
    context = {}
    return render(request, 'searchapp/index.html', context)
