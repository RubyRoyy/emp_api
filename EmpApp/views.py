

from rest_framework.views import APIView
from EmpApp.models import Emp
from EmpApp.serializers import EmpSerializer

from rest_framework.response import Response
from rest_framework import status


class EmpListView(APIView):
    def get(self,request):
        emp = Emp.objects.all()
        serializer = EmpSerializer(emp , many=True)
        return Response(serializer.data)

    def post(self,request):
        emp = request.data

        serializer = EmpSerializer(emp)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data ,
                    status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST)







from rest_framework.views import APIView
from .models import Emp
from .serializers import EmpSerializer

from rest_framework.response import Response

from  rest_framework import status
import json

class EmpView(APIView):
    def get(self,request):
        emps = Emp.objects.all()
        serializer = EmpSerializer(emps , many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)


    def post(self,request):
        serializer = EmpSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            # return Response({'message' : 'new object is added to Database'})
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)


class EmpDetails(APIView):
    def get_object_by_id(self,pk):
        try:
            emp = Emp.objects.get(empid=pk)
        except Emp.DoesNotExist:
            emp = None
        return emp


    def get(self,request,pk):
        # emp_data = Emp.objects.get(empid=pk)
        # serializer = EmpSerializer(emp_data)
        # return Response(serializer.data)

        emp = self.get_object_by_id(pk)

        if emp is None:
           return Response({'msg': 'Record is not available..Try again'},
                           status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = EmpSerializer(emp)
            return Response(serializer.data ,
                            status=status.HTTP_200_OK)



    def put(self,request,pk):
        emp = self.get_object_by_id(pk)

        if emp is None:
            return Response({'msg': 'Record is not available to updating.Try again...'},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = EmpSerializer(emp, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data ,
                            status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors ,
                            status=status.HTTP_400_BAD_REQUEST)




    def delete(self,request,pk):
        emp = self.get_object_by_id(pk)


        if emp is None:
            return Response({'msg': 'Record is not available to Deleting.Try another record...'},
                            status=status.HTTP_404_NOT_FOUND)

        emp.delete()
        return Response({'message' : 'Record deleted succefully'},
                        status = status.HTTP_204_NO_CONTENT)

