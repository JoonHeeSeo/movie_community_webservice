from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from accounts.models import User
from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def article_list(request):
    # 게시글 전체 조회
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    
    # 게시글 생성
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)        
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    # 게시글 상세 조회
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    # 게시글 삭제
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # 게시글 수정
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def article_likes(request, article_pk):
    # 게시글 좋아요
    if request.method == 'POST':
        article = get_object_or_404(Article, pk=article_pk)

        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
        else:
            article.like_users.add(request.user)

        serializer = ArticleSerializer(article)
        return Response(serializer.data)



@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def comment_list(request):
    # 댓글 전체 조회 (미사용, 데이터 체크 용도)
    if request.method == 'GET':
        comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    

@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    # 댓글 조회
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    # 댓글 삭제 
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # 댓글 수정
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, article_pk):
    # 댓글 생성
    if request.method == 'POST':
        article = get_object_or_404(Article, pk=article_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile_get(request, username):
    # 프로필 조회
    if request.method == 'GET':

        # username을 통해 userid를 조회
        user = User.objects.get(username=username)
        userid = user.id

        # userid가 일치하는 게시글 조회
        articles = Article.objects.filter(user_id=userid)
        articles_serializer = ArticleSerializer(articles, many=True)

        # userid가 일치하는 댓글 조회
        comments = Comment.objects.filter(user_id=userid)
        comments_serializer = CommentSerializer(comments, many=True)

        # serializing
        serializer = {
            'articles': articles_serializer.data if articles else [],
            'comments': comments_serializer.data if comments else [],
        }

        return Response(serializer)





