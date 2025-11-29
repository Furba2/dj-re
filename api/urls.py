from django.urls import path
from . import views

urlpatterns = [
    path('topics/', views.TopicListCreate.as_view()),
    path('topics/<int:pk>/', views.TopicRetrieveUpdateDestroy.as_view()),
]