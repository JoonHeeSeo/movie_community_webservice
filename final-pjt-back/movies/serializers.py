from rest_framework import serializers
from .models import Movie, Comment
from accounts.models import User


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'
        # fields = ('id', 'title', 'content')


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article', 'user',)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'