from rest_framework import serializers
from . import models


# Each field in a Form class is responsible not only for validating data, but also for "cleaning" it — normalizing it to a consistent format.
# Serializer fields handle converting between primitive values and internal datatypes.
# They also deal with validating input values, as well as retrieving and setting the values from their parent objects.

# Serializer - kod który pozwala na łatwe przekonwertowanie data inputs w Python objects. Coś jak JSON.parse(), albo app.json(), czyli konwertujemy JSON w JS/Python obiekt i na odwrót.
# Serializer -> Odpowiada za serializację, ale też validację data którą otrzymujemy. W Mongoose to Model był odpowiedzialny za validację, tutaj Serializers odpowiadają za validację i konwersję danych.
# Model -> Opisuje tablicę w naszej DB, to blueprint, jak w DB będzie zapisany konkretny obiekt
# Manager -> Zawiera metody takie jak create, update itd. Odpowiada za działania w bazie danych. Możemy te metody napisywać.

# Serializer is very similar to Django forms
# Whenever a POST, PUT or PATCH requests is made, expect an input with name, and validate that input to a maximum length of 10
class HelloSerializer(serializers.Serializer):
    """ Serializes a nane field for testing our APIView """
    name = serializers.CharField(max_length=10)


# The way that we work with model serializers is we use the Meta Class to configure the serializer to point to a specific model in our project
class UserProfileSerializer(serializers.ModelSerializer):
    """ Serializes a user profile object """

    class Meta:
        model = models.UserProfile
        # Serializer fields handle converting between primitive values and internal datatypes.
        # They also deal with validating input values, as well as retrieving and setting the values from their parent objects.
        fields = ('id', 'name', 'email', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'min_length': 8,
                'style': {'input_type': 'password'}
            }
        }

    # Whenever we create a new object with our UserProfileSerializer, it will validate the fields provided to the serializer, and then it will call the create function, passing in the validated data.
    # From Mark: The Django REST Framework ModelSerializer has a default create() function which is used for creating standard objects.
    # From Mark: By default, it simply takes all the fields provided and passes them into the create() function of the model set in the Meta class.
    def create(self, validated_data):
        """ Create and return a new user """
        user = models.UserProfile.objects.create_user(name=validated_data['name'],
                                                      email=validated_data['email'],
                                                      password=validated_data['password'])

        # The object returned by create is then serialized as the response (with the 201 status) which is why it is required and not just optional.
        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)

    # def validate(self, data):
    #     if len(data['password']) < 8:
    #         raise serializers.ValidationError('Password must have at least 8 characters.')


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """ Serializers profile feed items """

    class Meta:
        model = models.ProfileFeedItem
        # id and created_on are by default set up by Django as read-only. They are created by the DB
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {
            'user_profile': {
                'read_only': True,
            }
        }
