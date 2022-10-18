from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title',)

def global_funcion():
    return ' global인데...'

class ArticleSerializer(serializers.ModelSerializer):
    class CommentSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = Comment
            fields = ('id', 'content')
            read_only_fields = ('article',)

    comment_set = CommentSerializer(
        many=True,
        read_only=True,
    )
    comment_count = serializers.IntegerField(
        source='comment_set.count',
        read_only=True,
    )
    add_data = serializers.SerializerMethodField(method_name='my_method')

    class Meta:
        model = Article
        fields = '__all__'

    def my_method(self, obj):
        return '>>>' + obj.title + '이게 되나?' + '<<<' + global_funcion()


class CommentSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)



