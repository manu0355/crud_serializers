from django.shortcuts import render
from CRUDserial.models import Student,School
from CRUDserial.serializers import StudentSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView 

# Create your views here.


class Student_details(APIView):
    def get(self,request):
        stu_obj= Student.objects.all()
        studserialobj= StudentSerializer(stu_obj,many=True)
        return Response(studserialobj.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializeobj=StudentSerializer(data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(serializeobj.data, status=status.HTTP_201_CREATED)
        return Response(serializeobj.error, status=status.HTTP_400_BAD_REQUEST)

class Student_detailsview(APIView):
    def get(self,request,id):
        one_stu= Student.objects.get(id=id)
        onestu_serial= StudentSerializer(one_stu)
        return Response(onestu_serial.data, status=status.HTTP_200_OK)