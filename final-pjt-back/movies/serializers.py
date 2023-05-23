from rest_framework import serializers
from .models import Movie
from accounts.models import User

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'
        # fields = ('id', 'title', 'content')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'