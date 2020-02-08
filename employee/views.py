from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializers import GetAllEmployeeSerializer, EmployeeSerializer
# Create your views here.

class GetAllEmployeeAPIView(APIView):
    def get(self, request):
        list_emp = Employee.objects.all()
        mydata = GetAllEmployeeSerializer(list_emp, many = True)
        return Response(data = mydata.data, status = status.HTTP_200_OK)
    
    def post(self, request):
        mydata = EmployeeSerializer(data=request.data)
        if not mydata.is_valid():
            return Response('sai du lieu roi',status=status.HTTP_400_BAD_REQUEST)
        title = mydata.data['title1']
        price = mydata.data['price1']
        content = mydata.data['content1']
        cs = Employee.objects.create(title=title, price=price,content=content)
        return Response(data=cs.id,status=status.HTTP_200_OK)

