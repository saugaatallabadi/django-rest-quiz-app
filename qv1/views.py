from django.shortcuts import render
from rest_framework.views import APIView
from qv1.models import Question, Quiz
from qv1.serializers import QuestionSerializer, QuizSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets

# Create your views here.


# class Quizzes(APIView):

#     def get_object(self):
#         try:
#             return Quiz.objects.all()
#         except Quiz.DoesNotExist:
#             raise status.HTTP_404_NOT_FOUND

#     def get(self, request, format=None):
#         # queryset = Quiz.objects.all()  # Grabs all rows
#         queryset = self.get_object()  # Grabs all rows
#         serializer = QuizSerializer(queryset, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = QuizSerializer(data=request.data)
#         try:
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#         except Exception as e:
#             print(e)
#             return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

#     def delete(self, request):
#         # Send this www-form-urlencoded / JSON
#         queryset = Quiz.objects.get(id=request.data['id'])
#         queryset.delete()
#         return Response(data='Delete', status=status.HTTP_410_GONE)

#     def put(self, request):
#         quiz = Quiz.objects.get(id=request.data['id'])
#         serializer = QuizSerializer(quiz, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
#         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


# Done with GET and POST in 1 ListCreateAPIView
# For only GET- Use ListAPIView
# class QuizView(generics.ListCreateAPIView):
#     queryset = Quiz.objects.all()
#     serializer_class = QuizSerializer


# class QuizView(generics.RetrieveDestroyAPIView):
#     queryset = Quiz.objects.all()
#     serializer_class = QuizSerializer
#     lookup_field = 'pk'

class QuizView(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
