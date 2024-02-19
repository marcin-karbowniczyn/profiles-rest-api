from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.http import HttpResponseRedirect

from . import serializers
from . import models
from . import permissions


class UserProfileViewSet(viewsets.ModelViewSet):
    """ Handle creating and updating profiles """
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """ Handles creating, reading, and updating profile feed items """
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.UpdateOwnStatus, IsAuthenticated)  # IsAuthenticatedOrReadOnly -> Must be authenticated if making something else than a GET request

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return HttpResponseRedirect(redirect_to='/api/feed/')

    def perform_create(self, serializer):
        """ Sets the user profile to the logged-in user """
        serializer.save(user_profile=self.request.user)  # user_profile = foreignKey


class UserLoginAPIView(ObtainAuthToken):
    """ Handle creating user authentication tokens """
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
