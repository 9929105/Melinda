from rest_framework import serializers

from .models import Nomenclature, Textmap


class NomenclatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nomenclature
        
        
        
class TextmapSerializer(serializers.ModelSerializer):
    nomenclature = NomenclatureSerializer()

    class Meta: 
        depth = 2
        model = Textmap
