from django.shortcuts import render
from django.http.response import HttpResponse
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,AllowAny
from dropbox.models import Profile,Vault,File
from dropbox import serializers
from rest_framework.decorators import api_view, permission_classes,action
# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404,get_list_or_404


class UserViewSet(viewsets.ModelViewSet):
    """Manager for custom user"""
    model = Profile
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer

    def retrieve(self,request,*args,**kwargs):
        queryset = Profile.objects.all()
        # queryset2 = Profile.objects.filter(pk=request.user.id)
        profile = get_object_or_404(queryset,pk=request.user.id)
        serializer = serializers.ProfileSerializer(profile)
        return Response(serializer.data)

    def get_object(self):
        """Overwrite update method, unnesessary to get pk in URL"""
        return self.model.objects.get(pk=self.request.user.pk)


class UserList(generics.ListCreateAPIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """
    queryset = Profile.objects.all()
    serializer_class = serializers.UserSerializerWithToken
    permission_classes = (AllowAny,)
    authentication_classes = ()

    def post(self, request, *args, **kwargs):
        serializer = serializers.UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VaultList(viewsets.ModelViewSet):
    model = Vault
    queryset = Vault.objects.all()
    serializer_class = serializers.VaultSerializer

    def list(self,request,*args,**kwargs):
        queryset = Vault.objects.filter(owner_id=request.user.id)
        serializer = serializers.VaultSerializer(queryset,many=True)
        return Response(serializer.data)

    def get_object(self):
        'Overwrite update method, unnesessary to get pk in URL'
        return self.model.objects.get(pk=self.request.user.pk)


class VaultDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Vault
    queryset = Vault.objects.all()
    serializer_class = serializers.VaultSerializer