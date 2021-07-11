from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class Sample_Class(APIView):
    def post(self,request):
        print('changed applied')
        return Response('post method called')
