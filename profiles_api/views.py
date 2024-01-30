from rest_framework.views import APIView
from rest_framework.response import Response


# APIView expexts a function for the different HTTP requests that can be made to the view.
class HelloAPIView(APIView):
    """ Test API View """

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
        return Response({'message': 'Hello', 'an_apiview': an_apiview})
