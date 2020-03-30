# This file contains views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

@api_view(['GET', 'POST'])
def index(request): # Function based view
    # message = 'This URL is at index'
    print(request.user)
    print(request.auth)
    if request.method == 'GET':
        return Response(data={'message': 'Hello Django2'}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        print(request.data)
        return Response(data=request.data,  status=status.HTTP_200_OK)
    else:
        return Response(data="Request Method is Not Right")

class Message(APIView):
    def get(self, request):
        print("Hit by API Call")
        return Response(data="This is the class based view (GET)", status=status.HTTP_200_OK)

    def post(self, request):
        print("Hit by POST API Call")
        print(request.data)
        return Response(data="This is the class based view (POST)", status=status.HTTP_200_OK)
