from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='index'),
  
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('service/', views.service, name="service"),
    path('service_detail/<str:pk>', views.service_detail,name='service_detail'),
    path('message', views.messages, name="message"),
    
    
    
    #download brochure
    path('download/', views.download, name="download"),
  
  
]
