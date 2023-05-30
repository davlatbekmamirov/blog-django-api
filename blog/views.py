from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


from .models import BlogModel
from .serializers import BlogModelSerializer


class BlogView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, *args, **kwargs):
        blogs = BlogModel.objects.all()
        serializer = BlogModelSerializer(blogs, many=True)

        return Response(serializer.data)


class BlogDetailView(APIView):

    def get(self, request, *args, **kwargs):
        blog_detail = get_object_or_404(BlogModel, pk=kwargs.get("pk"))
        serializer = BlogModelSerializer(blog_detail)
        return Response(serializer.data)
