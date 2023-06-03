from rest_framework import viewsets
from bitrix.models import *
from bitrix.serializers import *
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated

class TagatViewSet(viewsets.ModelViewSet):
    queryset = Tagat.objects.all()
    serializer_class = TagatSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('inn',)

class TdataViewSet(viewsets.ModelViewSet):
    queryset = Tdata.objects.all()
    serializer_class = TdataSerializer
    filter_backends = (filters.SearchFilter,)

class TemailViewSet(viewsets.ModelViewSet):
    queryset = Temail.objects.all()
    serializer_class = TemailSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('inn',)

class TklientViewSet(viewsets.ModelViewSet):
    queryset = Tklient.objects.all()
    serializer_class = TklientSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('inn',)

class TtarifViewSet(viewsets.ModelViewSet):
    queryset = Ttarif.objects.all()
    serializer_class = TtarifSerializer
    filter_backends = (filters.SearchFilter,)


class Twialon100ViewSet(viewsets.ModelViewSet):
    queryset = Twialon100.objects.all()
    serializer_class = Twialon100Serializer
    filter_backends = (filters.SearchFilter,)
