from rest_framework import serializers

from .models import Nomenclature, Textmap


class NomenclatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nomenclature
        #fields=('code_identifier', 'display', 'coding_system', 'popularity')
        
class TextmapSerializer(serializers.ModelSerializer):
    nomenclature = NomenclatureSerializer()

    class Meta: 
        depth = 2
        model = Textmap
