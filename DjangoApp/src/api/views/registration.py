from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from api.serializer import *
from api.helper_functions import generate_excelid as gen


class CollegeList(ListCreateAPIView):
    """
    Retrieve list of all colleges
    Create a new college name if it doesn't exist
    """
    queryset = College.objects.all()
    serializer_class = CollegeSerializer


class CollegeDetails(ListAPIView):
    """
    This view return a list of all students registered
    from a college.
    """
    serializer_class = ExcelIdSerializer

    def get_queryset(self):
        try:
            pk = self.kwargs['pk']
            college = College.objects.get(pk=pk)
            students = college.students.all()
            return students
        except ObjectDoesNotExist:
            raise NotFound()

class ExcelIdDetails(ListCreateAPIView):
    """
    GET:Retrieve student details with excelid,name,phone_number or email"
    POST:Create ExcelID for given student details
    """
    serializer_class = ExcelIdSerializer

    def get_queryset(self):
        excelid = self.request.query_params.get('excel_id', None)
        name = self.request.query_params.get('name', None)
        email = self.request.query_params.get('email', None)
        phone_number = self.request.query_params.get('phone_number', None)

        if excelid:
            return ExcelID.objects.filter(pk=excelid)
        if name:
            return ExcelID.objects.filter(name__contains=name)
        if excelid:
            return ExcelID.objects.filter(email=email)
        if excelid:
            return ExcelID.objects.filter(phone_number=phone_number)
    
    def post(self, request, format=None):
        request.data['id'] = gen.generate()
        serializer = ExcelIdSerializer(data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)