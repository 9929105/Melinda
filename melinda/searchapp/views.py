import django_filters
from django.shortcuts import render

from rest_framework import viewsets, filters

from .models import Nomenclature, Textmap
from .serializers import NomenclatureSerializer, TextmapSerializer 



class NomenclatureViewSet(viewsets.ModelViewSet):
    queryset = Nomenclature.objects.all()
    serializer_class = NomenclatureSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('display','attribute_string',)
    paginate_by = 5000

class TextMapViewSet(viewsets.ModelViewSet):
    queryset = Textmap.objects.all()
    serializer_class = TextmapSerializer


def index(request):
    context = {}
    return render(request, 'searchapp/index.html', context)

