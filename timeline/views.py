from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializer import *
from .filters import *

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    http_method_names = ['get', 'post']
    permission_classes = [IsAuthenticated]

    def create(self, request):
        content = request.data.get('content', None)
        author_id = request.user.id
        serializer = PostSerializer(data={'content': content, 'author': author_id})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filterset_class = CommentFilter
    http_method_names = ['get', 'post']
    permission_classes = [IsAuthenticated]

    def create(self, request):
        content = request.data.get('content', None)
        post_id = request.data.get('post', None)
        author_id = request.user.id
        serializer = CommentSerializer(data={'content': content, 'author': author_id, 'post': post_id})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LikeViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    http_method_names = ['post', 'delete']
    permission_classes = [IsAuthenticated]

    def create(self, request):
        post_id = request.data.get('post', None)
        author_id = request.user.id
        serializer = LikeSerializer(data={'author': author_id, 'post': post_id})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)