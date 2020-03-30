from django.urls import path
# from qv1.views import Quizzes
from qv1.views import QuizView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'quizzes', QuizView, basename='quiz')

# urlpatterns = [
#     # path('quizzes', Quizzes.as_view(), name='quizzes'),
#     path('quizzes', QuizView.as_view(), name='quizview'),

# ]

urlpatterns = []
urlpatterns += router.urls
