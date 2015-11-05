import django_filters
from django.shortcuts import render

from rest_framework import viewsets, filters

from .models import Nomenclature, Textmap
from .serializers import NomenclatureSerializer, TextmapSerializer 
from django.http import HttpResponse
from django.contrib import admin  
from django.conf.urls import patterns  

import os
from django.conf import settings
from django.core.files import File
import json
from pprint import pprint
import requests
from django.views.i18n import null_javascript_catalog

class NomenclatureViewSet(viewsets.ModelViewSet):
    queryset = Nomenclature.objects.all()
    serializer_class = NomenclatureSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('display','attributes','coding_sys_cd',)
    paginate_by = 5000

class TextMapViewSet(viewsets.ModelViewSet):
    queryset = Textmap.objects.all()
    serializer_class = TextmapSerializer


def index(request):
    context = {}
    return render(request, 'searchapp/index.html', context)

def refreshdb(request):
    context = {}
    coding_sys_cd = "2.16.840.1.113883.6.96"
    coding_system = "SNOMED-CT"

    tmpNoms=[]
    with open(os.path.join(settings.PROJECT_ROOT, 'static','snomed_ct_core.txt'),'r') as data_file:    
        data_file.readline()
        for line in data_file.readlines():
            tup= line.partition("|")
            code = tup[0]
            disp=tup[2].partition("|")[0]
            tmpNoms.append((code,disp,''))
    
    
    r=requests.get('http://service.oib.utah.edu:8080/openInfobutton/assetManager/assets') 

    
    j_obj=r.json()
    for jo in j_obj:
        if jo['namespaceCd']==u'hsc.utah.edu':
            disp = jo['displayName']
            if jo['assetUrl']:
                url =  jo['assetUrl']
            else:
                url=''
            
            tmpNoms.append((disp, disp, url))
    
    
    for nom in tmpNoms:
        ids_row={}
        ids_row["code_identifier"]=nom[0]
        ids_row["coding_sys_cd"]=coding_sys_cd
        defaults={}
        defaults["code_identifier"]=nom[0]
        defaults["display"]=nom[1]
        defaults["coding_system"]=coding_system
        defaults["coding_sys_cd"]=coding_sys_cd
        defaults["url"] = nom[2]
        if defaults["url"] !='':
            defaults["isExclusive"] = True
        instance, created = Nomenclature.objects.get_or_create(defaults=defaults, **ids_row)
        
        """    if instance:
            pprint(">>{0}".format(str(instance)))
        else:
            pprint("++{0}".format(str(created)))
        """ 
    
    
    r=requests.get('http://service.oib.utah.edu:8080/openInfobutton/assetManager/assets') 

    
    ids=[]
    j_obj=r.json()
    for jo in j_obj:
        if jo['namespaceCd']==u'hsc.utah.edu':
            ids.append(jo['assetId'])
            
    
    
    assets={}
    for i in ids:
        obj = requests.get('http://service.oib.utah.edu:8080/openInfobutton/assetManager/assetProperties/'+`i`+"/")
        for attr in obj.json():
            if attr['propertyName'] == u'mainSearchCriteria.v':
                code = attr['code']
                codeSys = attr['codeSystem']
                assets.setdefault(codeSys,[]).append(code)
                
                
    for codesys in assets.keys():
        for cd in assets[codesys]:
            noms = Nomenclature.objects.filter(coding_sys_cd=codesys).filter(code_identifier=cd)
            if noms.exists():
                for nom in noms:
                    nom.isExclusive = True
                    nom.save()
                    pprint(nom)
                
    return HttpResponse("done!")
    

    
  
    
