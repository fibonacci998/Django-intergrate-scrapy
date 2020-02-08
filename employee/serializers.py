from rest_framework import serializers
from .models import Employee
class GetAllEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'title', 'price', 'content')

class EmployeeSerializer(serializers.Serializer):
    title1 = serializers.CharField(max_length=50)
    price1 = serializers.IntegerField()
    content1 = serializers.CharField(max_length=50)

