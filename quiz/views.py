# This file contains views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def index(request): # Function based view
    message = 'This URL is at index'
    return Response(data=message, status=status.HTTP_200_OK)