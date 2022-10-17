# views.py

from .serializers import ArticleSerializer
from rest_framework.response import Response
from .models import Article

# 모든 게시글 목록 조회
@api_view(['GET'])
def article_list(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)