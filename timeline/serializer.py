from rest_framework import serializers
from django.contrib.auth.models import User

from .models import *
from userauth.serializer import UserSerializer

class PostSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField(read_only=True)
    def get_likes_count(self, obj):
        return obj.likes.count()

    liked = serializers.SerializerMethodField(read_only=True)
    def get_liked(self, obj):
        request = self.context.get('request', None)
        if not request or not request.user:
            return False
        try:
            like_obj = obj.likes.get(author=request.user.id)
            if like_obj:
                return True
        except:
            return False
        return False

    def to_representation(self, instance):
        data = super(PostSerializer, self).to_representation(instance)
        data['author'] = UserSerializer(instance.author).data
        return data

    class Meta:
        model = Post
        fields = ['id', 'author', 'content', 'created_at', 'likes_count', 'liked']


#--- Comment
class CommentSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super(CommentSerializer, self).to_representation(instance)
        data['author'] = UserSerializer(instance.author).data
        return data
    class Meta:
        model = Comment
        fields = ['id', 'author', 'content', 'post', 'created_at', ]

#--- Likes
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'author', 'post',]