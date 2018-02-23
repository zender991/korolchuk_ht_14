from django.conf.urls import url
from news import views
from django.urls import path


urlpatterns = [
    #path('<str:category_name>/', views.stories_from_category),
    #path('<str:category_name>/<int:story_id>/', views.story_details),
    path('execute/', views.get_data)
]