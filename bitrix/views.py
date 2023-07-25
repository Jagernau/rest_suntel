from rest_framework import viewsets
from bitrix.models import *
from bitrix.serializers import *
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from django.views.generic import ListView
from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response

class TagatViewSet(viewsets.ModelViewSet):
    queryset = Tagat.objects.all()
    serializer_class = TagatSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = [TokenAuthentication]

class TdataViewSet(viewsets.ModelViewSet):
    queryset = Tdata.objects.all()
    serializer_class = TdataSerializer
    filter_backends = (filters.SearchFilter,)
    permission_classes = (IsAuthenticated,)
    authentication_classes = [TokenAuthentication]

class TemailViewSet(viewsets.ModelViewSet):
    queryset = Temail.objects.all()
    serializer_class = TemailSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = [TokenAuthentication]

class TklientViewSet(viewsets.ModelViewSet):
    queryset = Tklient.objects.all()
    serializer_class = TklientSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('inn',)
    permission_classes = (IsAuthenticated,)
    authentication_classes = [TokenAuthentication]

class TtarifViewSet(viewsets.ModelViewSet):
    queryset = Ttarif.objects.all()
    serializer_class = TtarifSerializer
    filter_backends = (filters.SearchFilter,)
    permission_classes = (IsAuthenticated,)
    authentication_classes = [TokenAuthentication]


class Twialon100ViewSet(viewsets.ModelViewSet):
    queryset = Twialon100.objects.all()
    serializer_class = Twialon100Serializer
    filter_backends = (filters.SearchFilter,)
    permission_classes = (IsAuthenticated,)
    authentication_classes = [TokenAuthentication]


class MergeEmailListView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        queryset = Temail.objects.filter(inn__isnull=False, kpp__isnull=False)
        data = []
        for email in queryset:
            try:
                client = Tklient.objects.get(inn=email.inn, kpp=email.kpp)
                data.append({
                    'name': client.name,
                    'email': email.email
                })
            except Tklient.DoesNotExist:
                pass
        return Response(data)
