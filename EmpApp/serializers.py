

from rest_framework.serializers import ModelSerializer
from EmpApp.models import Emp

class EmpSerializer(ModelSerializer):
    class Meta :
        model = Emp
        fields = '__all__'




















# from rest_framework import serializers
# from .models import Emp
#
# class EmpSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Emp
#         fields = ['empid', 'empname', 'salary']
#
