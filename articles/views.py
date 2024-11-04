from .models import Article, Like
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.


@api_view(http_method_names=["GET"])
def get_like_count(request, article_id):
    article = Article.objects.filter(pk=article_id).first()
    if not article:
        return Response(
            {"status": "error", "message": "Article not found"},
            status=status.HTTP_404_NOT_FOUND,
        )

    like, created = Like.objects.get_or_create(article=article)

    return Response(
        {"status": "success", "data": {"like_count": like.count}},
        status=status.HTTP_200_OK,
    )


@api_view(http_method_names=["POST"])
def like_article(request, article_id):
    article = Article.objects.filter(pk=article_id).first()
    if not article:
        return Response(
            {"status": "error", "message": "Article not found"},
            status=status.HTTP_404_NOT_FOUND,
        )

    like, created = Like.objects.get_or_create(article=article)

    like.count += 1
    like.save()

    return Response(
        {"status": "success", "data": {"like_count": like.count}},
        status=status.HTTP_200_OK,
    )
