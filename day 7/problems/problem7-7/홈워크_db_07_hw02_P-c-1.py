# c- serializers.py
from numpy import source


class ArticleSerializer(serializers.ModelSerializer):
    commnet_count = serializers.IntegerField(
        source='comment_set.count',
        read_only=True,
    )

    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'commnet_count',)