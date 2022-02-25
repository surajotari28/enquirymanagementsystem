from rest_framework import serializers
from . models import (CourseModel, EnquiryModel)

class EnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = EnquiryModel
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    enquiry = EnquirySerializer(many=True, read_only=True)
    class Meta:
        model = CourseModel
        fields = '__all__'
        
