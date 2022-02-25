from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CourseModel(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=150)
    duration = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return self.name
    
class EnquiryModel(models.Model):
    login_user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE, related_name="enquiry", blank=False)
    user_first_name = models.CharField(max_length=50)
    user_last_name = models.CharField(max_length=50)
    phone_number = models.IntegerField(null=False, unique=True)
    enquiry = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    enqupdated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user_first_name