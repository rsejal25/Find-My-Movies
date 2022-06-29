from rest_framework import serializers
from .models import Play_List,Logging_User,Movies


class LogginUserSerializer(serializers.ModelSerializer):
 class Meta:
  fields='__all__'
  model=Logging_User

class MovieSerializer(serializers.ModelSerializer):
 class Meta:
  fields='__all__'
  model=Movies


class PlayListSerializer(serializers.ModelSerializer):
 class Meta:
  model=Play_List
  fields='__all__'