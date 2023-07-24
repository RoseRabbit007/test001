from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import*
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

# Create your views here.

class StudentView(APIView):
    def post(self, request):
        serializer=StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data},status=status.HTTP_200_OK)
        else:
            return Response({"status":"error","data":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        
____________________asdfghjkl______________
____________________asdfghjkl______________
____________________asdfghjkl______________
____________________asdfghjkl______________
____________________asdfghjkl______________
____________________asdfghjkl_vvvvv_____________

    def get(self,request,id=None):
        if id:
            data=Student.objects.get(id=id)
            serializer= StudentSerializers(data)
            return Response({"status":"success","data": serializer.data},status= status.HTTP_200_OK)
        data = Student.objects.all()
        serializer = StudentSerializers(data, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    
    def patch(self,request,id=None):
        data = Student.objects.get(id=id)
        serializer = StudentSerializers(data, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"successfully update","data":serializer.data})
        else:
            return Response({"status":"error","data":serializer.errors})
        
    def delete(self,request,id=None):
        data=get_object_or_404(Student, id=id)
        data.delete()
        return Response({"status":"successfully deleted","data":"data deleted"})



    
        
        

    


