from django.urls import path
from . import views

urlpatterns = [
    path('topics/', views.TListCreate.as_view()),
    path('topics/<int:pk>/', views.TRetrieveUpdateDestroy.as_view()),
]