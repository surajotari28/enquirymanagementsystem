from django.contrib import admin
from . models import (CourseModel, EnquiryModel)
# Register your models here.

@admin.register(CourseModel)
class CourseModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'about', 'duration', 'price')
    
@admin.register(EnquiryModel)
class EnquiryModelAdmin(admin.ModelAdmin):
    list_display = ('course', 'user_first_name', 'user_last_name', 'phone_number', 'enquiry', 'created', 'enqupdated')
