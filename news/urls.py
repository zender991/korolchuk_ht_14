from news import views
from django.urls import path,re_path


urlpatterns = [
    path('execute/', views.get_data),
    path('<str:category_name>/<int:story_id>/', views.story_details),
    path('<str:category_name>/', views.stories_from_category),
    path('', views.index)
]