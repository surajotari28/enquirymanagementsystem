from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('courselist', views.Course_List, basename='course_list'),
router.register('enquirylist', views.Enquiry_List, basename='Enquiry_List')

urlpatterns = [
    path('', include(router.urls)),
    
    # path('list/', views.Course_List.as_view(), name='course_list'),
    # path('list/<int:pk>/', views.Course_Details.as_view(), name='course_details'),
    
    # path('list/<int:pk>/enquiry/', views.Enquiry_List.as_view(), name='course_list'),
    # path('list/enquiry/<int:pk>/', views.Enquiry_Details.as_view(), name='Enquiry_detail'),
    
]