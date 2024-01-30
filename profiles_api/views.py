from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers


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
            message = f'Hello {name}'
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
