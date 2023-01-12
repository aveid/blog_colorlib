from rest_framework.pagination import PageNumberPagination


class BlogListPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'nazi'
    # max_page_size = 10000