from django.urls import path
from .views import (
    TaskListCreateView, TaskDetailView,
    EntityListCreateView, EntityDetailView,
    FieldDefinitionListCreateView, FieldDefinitionDetailView,
    IntegrationLogListCreateView, IntegrationLogDetailView
)

urlpatterns = [
    # Task endpoints
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),

    # Entity endpoints
    path('entities/', EntityListCreateView.as_view(), name='entity-list-create'),
    path('entities/<int:pk>/', EntityDetailView.as_view(), name='entity-detail'),

    # FieldDefinition endpoints
    path('fields/', FieldDefinitionListCreateView.as_view(), name='field-list-create'),
    path('fields/<int:pk>/', FieldDefinitionDetailView.as_view(), name='field-detail'),

    # IntegrationLog endpoints
    path('logs/', IntegrationLogListCreateView.as_view(), name='log-list-create'),
    path('logs/<int:pk>/', IntegrationLogDetailView.as_view(), name='log-detail'),
]
