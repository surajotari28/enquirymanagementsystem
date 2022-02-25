from tkinter import E
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from . permissions import LoginUserOrReadOnly, AdminOrReadOnly
from django.shortcuts import get_object_or_404
# from rest_framework import generics
from . models import (CourseModel, EnquiryModel)
from . serializers import (CourseSerializer, EnquirySerializer)

# Create your views here.

class Course_List(viewsets.ViewSet):
    permission_classes = [AdminOrReadOnly]
    def list(self, request):
        queryset = CourseModel.objects.all()
        serializer = CourseSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = CourseModel.objects.all()
        course = get_object_or_404(queryset, pk=pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    
    def create(self, request):
        permission_classes = [AdminOrReadOnly]
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def update(self, request, pk=None):
        permission_classes = [AdminOrReadOnly]
        queryset = CourseModel.objects.all()
        course = get_object_or_404(queryset, pk=pk)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def partial_update(self, request, pk=None):
        permission_classes = [AdminOrReadOnly]
        queryset = CourseModel.objects.all()
        course = get_object_or_404(queryset, pk=pk)
        serializer = CourseSerializer(course, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def destroy(self, request, pk=None):
        permission_classes = [AdminOrReadOnly]
        queryset = CourseModel.objects.all()
        delete = get_object_or_404(queryset, pk=pk)
        delete.delete()
        return Response({'message': 'data delete successfully'})
    
class Enquiry_List(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def list(self, request):
        queryset = EnquiryModel.objects.all()
        serializer = EnquirySerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = EnquirySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def retrieve(self, request, pk=None):
        queryset = EnquiryModel.objects.all()
        course = get_object_or_404(queryset, pk=pk)
        serializer = EnquirySerializer(course)
        return Response(serializer.data)
        
    def update(self, request, pk=None):
        queryset = EnquiryModel.objects.all()
        course = get_object_or_404(queryset, pk=pk)
        serializer = EnquirySerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def partial_update(self, request, pk=None):
        queryset = EnquiryModel.objects.all()
        course = get_object_or_404(queryset, pk=pk)
        serializer = EnquirySerializer(course, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def destroy(self, request, pk=None):
        queryset = EnquiryModel.objects.all()
        delete = get_object_or_404(queryset, pk=pk)
        delete.delete()
        return Response({'message': 'data delete successfully'})

# class Course_List(generics.ListCreateAPIView):
#     queryset = CourseModel.objects.all()
#     serializer_class = CourseSerializer
    
# class Course_Details(generics.RetrieveUpdateDestroyAPIView):
#     queryset = CourseModel.objects.all()
#     serializer_class = CourseSerializer
    
# class Enquiry_List(generics.ListCreateAPIView):
#     queryset = EnquiryModel.objects.all()
#     serializer_class = EnquirySerializer
    
# class Enquiry_Details(generics.RetrieveUpdateDestroyAPIView):
#     queryset = EnquiryModel.objects.all()
#     serializer_class = EnquirySerializer
