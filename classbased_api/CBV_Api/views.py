from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import student_serializer
from .models import Student
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class StudentApi(APIView):
    def get(self,request,pk=None,format=None):
        id = pk
        if id is not None:
            st=Student.objects.get(id=id)
            serializer=student_serializer(st)
            print(type(serializer),serializer)
            return Response(serializer.data,status=status.HTTP_200_OK)

        st=Student.objects.all()
        serializer=student_serializer(st,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
    
        serializer=student_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({"msg":"data successfullly created"},status=status.HTTP_201_CREATED)

    def put(self,request,pk=None,format=None):
            id=pk
            st=Student.objects.get(pk=id)
            serializer=student_serializer(st,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg":"Data sucessfully udated"},status=status.HTTP_201_CREATED)
            return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk=None,format=None):
            id=pk
            st=Student.objects.get(pk=id)
            serializer=student_serializer(st,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg":"Data sucessfully udated"})
            return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            st=Student.objects.get(pk=id)
            st.delete()
            return Response({"msg":"Data Successfully deleted"})

        return Response({"msg":"oh nooo"},status=status.HTTP_400_BAD_REQUEST)


