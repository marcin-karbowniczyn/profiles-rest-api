from rest_framework import serializers


# Serializer - kod który pozwala na łatwe przekonwertowanie data inputs w Python objects. Coś jak JSON.parse(), albo app.json(), czyli konwertujemy JSON w JS/Python obiekt i na odwrót.

# Serializers is very similar to Django forms
# Whenever a POST, PUT or PATCH requests is made, expect an input with name, and validate that input to a maximum length of 10
class HelloSerializer(serializers.Serializer):
    """ Serializes a nane field for testing our APIView """
    name = serializers.CharField(max_length=10)
