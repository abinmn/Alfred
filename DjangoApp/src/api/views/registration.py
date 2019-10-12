from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status

from api.serializer import *
from api.helper_functions import generate_excelid as gen

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


class CollegeDetails(ListAPIView):
    serializer_class = ExcelIdSerializer

    def get_queryset(self):
        """
        This view return a list of all students registered
        from a college.
        """
        pk = self.kwargs['pk']
        college = College.objects.get(pk=pk)
        students = college.students.all()
        return students

class ExcelIdDetails(APIView):
    # Retrieve participant details using excel_id/name/email/phone_number
    def get_object(self, request):
        excelid = request.query_params.get('excel_id', None)
        name = request.query_params.get('name', None)
        email = request.query_params.get('email', None)
        phone_number = request.query_params.get('phone_number', None)

        if excelid:
            return ExcelID.objects.filter(pk=excelid)
        if name:
            return ExcelID.objects.filter(name__contains=name)
        if excelid:
            return ExcelID.objects.filter(email=email)
        if excelid:
            return ExcelID.objects.filter(phone_number=phone_number)
        
    def get(self, request, format=None):
       search_results = self.get_object(request)
       serializer = ExcelIdSerializer(search_results, many=True)
       return Response(serializer.data)

    def post(self, request, format=None):
        request.data['id'] = gen.generate()
        serializer = ExcelIdSerializer(data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
