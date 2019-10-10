from django.shortcuts import render
from api.serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CollegeList(APIView):

    def get(self, request, format=None):
        colleges = College.objects.all()
        serializer = CollegeSerializer(colleges, many=True)
        return Response(serializer.data)

    #Add new colleges to list
    def post(self, request, format=None):
        serializer = CollegeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

