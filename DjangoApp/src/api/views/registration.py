from django.shortcuts import render
from api.serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class CollegeList(APIView):

    #get list of all colleges
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

class CollegeDetails(APIView):

    def get_object(self, pk):
        try:
            return College.objects.get(pk=pk)
        except:
            raise Http404
    #Get details of students in a college, 404 if college id not found
    def get(self, request, pk, format=None):
        college = self.get_object(pk)
        students = college.students.all()
        serializer = ExcelIdSerializer(students, many=True)
        return Response(serializer.data)