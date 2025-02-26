from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Question, Choice
from .serializers import QuestionSerializer

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class QuestionList(APIView):
    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)


# View to get details of a specific question by its ID
class QuestionDetail(APIView):
    def get(self, request, pk):
        question = Question.objects.get(pk=pk)  # Get a single question by its primary key
        serializer = QuestionSerializer(question)  # Serialize the question
        return Response(serializer.data)  # Return the data as JSON
