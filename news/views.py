from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from news.models import Story, Category
from news.serializers import StorySerializer, CategorySerializer
from news.get_data_from_api import execute

from django.shortcuts import redirect

@api_view(['GET'])
def stories_from_category(request, category_name):
    if request.method == 'GET':
        news = Story.objects.filter(category_name='%s' % category_name)
        serializer = StorySerializer(news, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def story_details(request, category_name, story_id):
    if request.method == 'GET':
        story = Story.objects.filter(category_name='%s' % category_name, id=story_id)
        serializer = StorySerializer(story, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


def get_data(request):
    execute()
    return redirect('/')

