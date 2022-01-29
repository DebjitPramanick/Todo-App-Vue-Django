from datetime import date
from django.shortcuts import render
from rest_framework import authentication
from rest_framework.decorators import authentication_classes, permission_classes
from .models import Task
from .serializers import TaskSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication, )
    permission_classes = (IsAuthenticated, )
    queryset = Task.objects.filter(created=date.today())
    serializer_class = TaskSerializer




