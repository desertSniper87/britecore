from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from insurance.models import Risk
from insurance.permissions import UserIsOwnerRisk
from insurance.serializers import UserSerializer, GroupSerializer, RiskSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class RiskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows risks to be viewed or edited.
    """
    queryset = Risk.objects.all()
    serializer_class = RiskSerializer

class RiskCreateAPIView(ListCreateAPIView):
    serializer_class = RiskSerializer

    def get_queryset(self):
        return Risk.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RiskDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = RiskSerializer
    queryset = Risk.objects.all()
    permission_classes = (IsAuthenticated, UserIsOwnerRisk)

