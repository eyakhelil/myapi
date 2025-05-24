from rest_framework import serializers
from .models import Task, Entity, FieldDefinition, IntegrationLog

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

        
class FieldDefinitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldDefinition
        fields = '__all__'

class EntitySerializer(serializers.ModelSerializer):
    # Affiche les champs dynamiques liés à une entité
    fields = FieldDefinitionSerializer(many=True, read_only=True)

    class Meta:
        model = Entity
        fields = ['id', 'name', 'fields']

class IntegrationLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntegrationLog
        fields = '__all__'
