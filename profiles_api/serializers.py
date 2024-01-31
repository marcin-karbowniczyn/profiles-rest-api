from rest_framework import serializers
from . import models


# Serializer - kod który pozwala na łatwe przekonwertowanie data inputs w Python objects. Coś jak JSON.parse(), albo app.json(), czyli konwertujemy JSON w JS/Python obiekt i na odwrót.
# Serializer -> Odpowiada za serializację, ale też validację data którą otrzymujemy. W Mongoose to Model był odpowiedzialny za validację, tutaj Serializers odpowiadają za validację i konwersję danych.
# Model -> Opisuje tablicę w naszej DB, to blueprint, jak w DB będzie zapisany konkretny obiekt
# Manager -> Zawiera metody takie jak create, update itd. Odpowiada za działania w bazie danych. Możemy te metody napisywać.

# Serializers is very similar to Django forms
# Whenever a POST, PUT or PATCH requests is made, expect an input with name, and validate that input to a maximum length of 10
class HelloSerializer(serializers.Serializer):
    """ Serializes a nane field for testing our APIView """
    name = serializers.CharField(max_length=10)


# The way that we work with model serializers is we use the Meta Class to configure the serializer to point to a specific model in our project
class UserProfileSerializer(serializers.ModelSerializer):
    """ Serializes a user profile object """

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    # Whenever we create a new object with our UserProfileSerializer, it will validate the fields provided to the serializer,
    # and then it will call the create function, passing in the validated data.
    def create(self, validated_data):
        """ Create and return a new user """
        user = models.UserProfile.objects.create_user(email=validated_data['email'],
                                                      name=validated_data['name'],
                                                      password=validated_data['password'])
        return user
