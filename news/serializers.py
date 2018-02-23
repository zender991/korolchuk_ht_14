from rest_framework import serializers
from news.models import Category, Story


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'category_name')



class StorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Story
        fields = ('id', 'author', 'descendants', 'story_id', 'score', 'text', 'time', 'title', 'type', 'category_name',
                  'url', 'category_id')