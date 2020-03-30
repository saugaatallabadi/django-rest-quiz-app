from rest_framework.serializers import ModelSerializer
from qv1.models import Quiz, Question


class QuizSerializer(ModelSerializer):
    class Meta:
        model = Quiz
        # fields = ('name', 'description')  # Shows these 2 fields only
        # exclude = ('url',) # Excludes URL
        fields = '__all__'


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
