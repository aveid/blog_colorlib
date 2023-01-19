from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("category-management", views.CategoryViewSet)

urlpatterns = [
    path("blogs/", views.BlogListCreateAPIView.as_view()),
    path("blogs/<int:pk>/", views.BlogUpdateDeleteGetAPIView.as_view()),
    path("categories/", views.CategoryListAPIView.as_view()),
    path("tags/", views.TagListAPIView.as_view()),
    path("tags/<int:pk>/", views.TagBlogListAPIView.as_view()),
    path("", include(router.urls)),
]