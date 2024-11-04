from django.urls import path
from .views import get_like_count, like_article

urlpatterns = [
    path("articles/<int:article_id>/likes/", get_like_count, name="get_like_count"),
    path("articles/<int:article_id>/like/", like_article, name="like_article"),
]
