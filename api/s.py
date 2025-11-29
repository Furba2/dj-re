from rest_framework import serializers
from ls.models import T

class TS(serializers.ModelSerializer):
    class Meta:
        model = T
        fields = ['topic', 'entry']