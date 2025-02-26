# polls/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # Home page route
    path('questions/', views.QuestionList.as_view(), name='question-list'),
    path('questions/<int:pk>/', views.QuestionDetail.as_view(), name='question-detail'),
]
