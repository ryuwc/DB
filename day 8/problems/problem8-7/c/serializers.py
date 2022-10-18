# 홈워크_db_08_hw02_P-c.py
# serializers.py

class MusicSerializer(serializers.ModelSerializer):
    comment_count = serializers.IntegerField(
        source='comment_set.count',
        read_only=True,
    )

    class Meta:
        model = Music
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'comment_count',)