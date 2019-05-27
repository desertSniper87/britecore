from django.contrib.auth.models import User, Group
from rest_framework import serializers

from insurance.models import Risk, RiskType


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class RiskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Risk
        fields = ('user', 'name', 'date_created', 'risk_type')

    def create(self, validated_data):
        """
        Create and return a new `Risk` instance, given the validated data.
        """
        return Risk.objects.create(**validated_data)


    # def update(self, instance, validated_data):
    #        """
    #        Update and return an existing `Snippet` instance, given the validated data.
    #        """
    #        instance.title = validated_data.get('title', instance.title)
    #        instance.code = validated_data.get('code', instance.code)
    #        instance.linenos = validated_data.get('linenos', instance.linenos)
    #        instance.language = validated_data.get('language', instance.language)
    #        instance.style = validated_data.get('style', instance.style)
    #        instance.save()
    #        return instance
