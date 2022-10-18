# 홈워크_db_08_hw02_P-b-1.py
# serializers.py 

class MusicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'comment_set')