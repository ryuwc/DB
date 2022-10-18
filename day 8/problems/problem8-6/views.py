# 홈워크_db_08_hw01_P-2.py
# views.py

from .serializers import MusicListSerializer
from rest_framework.response import Response


@api_view(['GET'])
def music_list(request):
    musics = Music.objects.all()
    serializer = MusicListSerializer(musics, many=True)
    return Response(serializer.data)