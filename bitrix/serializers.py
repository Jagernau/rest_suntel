from rest_framework import serializers
from bitrix.models import *

class TagatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tagat
        fields = '__all__'

class TdataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tdata
        fields = '__all__'

class TemailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temail
        fields = '__all__'

class TklientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tklient
        fields = '__all__'

class TtarifSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ttarif
        fields = '__all__'

class Twialon100Serializer(serializers.ModelSerializer):
    class Meta:
        model = Twialon100
        fields = '__all__'
