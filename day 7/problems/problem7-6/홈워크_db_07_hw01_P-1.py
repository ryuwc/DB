# serializers.py
# serializer <===> form
# ArticleForm 정의할 때 ModelForm상속받아서 정의
# ArticleSerializer 정의 할 때 ModelSerializer상속받아서 정의

from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'