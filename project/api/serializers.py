from rest_framework import serializers


class ModelDataSerializer(serializers.Serializer):
    PARAMETER_1 = serializers.FloatField()
    PARAMETER_2 = serializers.FloatField()
    PARAMETER_3 = serializers.FloatField()
