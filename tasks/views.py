from rest_framework import generics
from rest_framework import viewsets
from .models import Task, Entity, FieldDefinition, IntegrationLog
from .serializers import TaskSerializer, EntitySerializer, FieldDefinitionSerializer, IntegrationLogSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# ----------- Entity Views -----------
class EntityListCreateView(generics.ListCreateAPIView):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer

class EntityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer

# ----------- FieldDefinition Views -----------
class FieldDefinitionListCreateView(generics.ListCreateAPIView):
    queryset = FieldDefinition.objects.all()
    serializer_class = FieldDefinitionSerializer

class FieldDefinitionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FieldDefinition.objects.all()
    serializer_class = FieldDefinitionSerializer

# ----------- IntegrationLog Views -----------
class IntegrationLogListCreateView(generics.ListCreateAPIView):
    queryset = IntegrationLog.objects.all()
    serializer_class = IntegrationLogSerializer

class IntegrationLogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IntegrationLog.objects.all()
    serializer_class = IntegrationLogSerializer
