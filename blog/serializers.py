from rest_framework import serializers

from .models import BlogModel


class BlogModelSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = BlogModel
        fields = ('id', 'title', 'body', 'summary', 'author')


