from django.db.models import Q
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Blog, Category, Tag
from blog.paginations import BlogListPagination
from blog.permissions import IsAuthorOrReadOnly
from blog.serializers import BlogSerializer, CategorySerializer, TagSerializer


class BlogListCreateAPIView(generics.ListCreateAPIView):
    pagination_class = BlogListPagination
    serializer_class = BlogSerializer
    permission_classes = [IsAuthorOrReadOnly, ]

    def get_queryset(self):
        search = self.request.query_params.get("search")
        queryset = Blog.objects.all()
        if search:
            queryset = queryset.filter(Q(title__icontains=search) |
                                       Q(description__icontains=search) |
                                       Q(category__title__icontains=search))
        return queryset

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


class TagListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthorOrReadOnly, ]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagBlogListAPIView(APIView):
    permission_classes = [IsAuthorOrReadOnly, ]
    def get(self, request, pk):
        queryset = Tag.objects.get(id=pk)
        serializer = BlogSerializer(queryset.blog.all(), many=True)
        return Response(serializer.data)


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny, ]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    @action(detail=False, methods=["get"])
    def new(self, request,):
        price_from = request.query_params.get("price_from")
        price_to = request.query_params.get("price_to")
        queryset = self.get_queryset()
        if price_from and price_to:
            queryset = queryset.filter(price__gte=price_from, price__lte=price_to)
        if price_from:
            queryset = queryset.filter(price__gte=price_from)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

