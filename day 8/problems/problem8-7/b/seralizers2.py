# 홈워크_db_08_hw02_P-b-2.py
# serializers.py

class MusicSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Music
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'comment_set')