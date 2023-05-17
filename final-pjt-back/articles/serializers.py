from rest_framework import serializers
from .models import Article, Comment

class ArticleListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = ('id', 'title', 'content')

class CommentSerializer(serializers.ModelSerializer):
    pass

class ArticleSerializer(serializers.ModelSerializer):
    # comment_set = CommentSerializer(many=True, read_only=True)
    # comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
