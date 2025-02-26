from rest_framework import serializers
from .models import Question, Choice

# Serializer for Choice model
class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'choice_text', 'votes']  # Fields you want to expose

# Serializer for Question model
class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)  # Serialize related choices for each question
    
    class Meta:
        model = Question
        fields = ['id', 'question_text', 'pub_date', 'choices']  # Fields you want to expose
