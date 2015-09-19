from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.models import User

from rest_framework import routers, serializers, viewsets

from searchapp import views


admin.autodiscover()
router = routers.DefaultRouter()
router.register(r'textmap', views.TextMapViewSet)
router.register(r'nomenclature',views.NomenclatureViewSet)

urlpatterns = patterns('',
    url(r'^$', views.index),

    url(r'^api/', include(router.urls)),
    url(r'^api-auth/',include('rest_framework.urls', namespace='rest_framework')),

    url(r'^admin/', include(admin.site.urls)),
)
