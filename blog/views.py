from rest_framework import generics

from blog.models import Blog
from blog.permissions import IsAuthorOrReadOnly
from blog.serializers import BlogSerializer


class BlogListCreateAPIView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthorOrReadOnly, ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class BlogUpdateDeleteGetAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthorOrReadOnly, ]
