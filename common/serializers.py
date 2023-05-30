from rest_framework import serializers

from .models import CommentModel, LikeModel, DisLikeModel


class CommentModelSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = CommentModel
        fields = ('id', 'body', 'author', 'blog')


class LikeModelSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = LikeModel
        fields = ('id', 'blog', 'author')


class DisLikeModelSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = DisLikeModel
        fields = ('id', 'blog', 'author')
