from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from . import serializers
from . import models
from . import permissions


# APIView -> takes functions that map to HTTP methods (GET, POST, PATCH etc.)
# ViewSets -> takes functions that map to common API actions (list, create, update, destroy)
# The main difference is that an APIView can handle a single HTTP request, while a Viewset can handle multiple HTTP requests.

# Behind the scenes the ModelViewSet will handle the request, pass the data into the serializer, and then call the create() method on the serializer instance.
# Then, the created object is returned back to the ViewSet in-case any further processing is required.
class UserProfileViewSet(viewsets.ModelViewSet):
    """ Handle creating and updating profiles """
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')


# Vid. 55
class UserLoginAPIView(ObtainAuthToken):
    """ Handle creating user authenticatio tokens """
    # We add this line to enable HTML view to be rendered in a browser
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


# APIView expexts a function for the different HTTP requests that can be made to the view.
class HelloAPIView(APIView):
    """ Test API View """
    serializer_class = serializers.HelloSerializer

    # Format is used to add format suffix, to the end of the endpoint URL. If you don't use it, best pratice is to set it to None.
    def get(self, request, format=None):
        """ Returns a list of APIView features """
        an_apiview = ['Uses HTTP methods as function (get, post, patch, put, delete)',
                      'Is similar to a traditional Django View, but was specifically intended to be used with APIs',
                      'Gives you the most control over your app logic',
                      'Is mapped manually to URLs'
                      ]

        # Every HTTP function (get, patch etc.) must return a return object.
        # Response needs to contain a disctionary or a list which it will then convert it to JSON.
        # Response will return status 200 by default
        # The Response class subclasses Django's SimpleTemplateResponse, that's why it renders a default template.
        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """ Create a hello message with our name """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        # I could set the status code as integer, but is a good practice to use status object, because I can easily tell what the request means by looking at the code.
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PUT request will update the entire object with what you've provided in the request
    # This is essentialy replacing an object with the object that was provided
    def put(self, request, pk=None):
        """ Handle updating an object """
        return Response({'method': 'PUT'})

    # PUT request would update only the fields that were provided in the request
    def patch(self, request, pk=None):
        """ Handle a partial update of an object """
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """ Delete an object """
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """ Test API Viewset """
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """ Return a hello msg """
        a_viewset = [
            'User actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',

        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """ Create a new hello msg """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """ Handle getting an object by its id """
        return Response({'http_method': 'GET'})

    # Function update maps to an PUT HTTP method/request.
    def update(self, request, pk=None):
        """ Handle updating an object """
        return Response({'http_method': 'PUT'})

    def partial(self, request, pk=None):
        """ Handle updating part of an object -> PATCH """
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """ Handle deleting an object """
        return Response({'http_method': 'DELETE'})
