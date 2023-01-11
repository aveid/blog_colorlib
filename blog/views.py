from rest_framework import generics

from blog.models import Blog, Category
from blog.permissions import IsAuthorOrReadOnly
from blog.serializers import BlogSerializer, CategorySerializer


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


class CategoryListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthorOrReadOnly, ]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer