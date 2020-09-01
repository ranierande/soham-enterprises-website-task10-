from django.urls import path
from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.index,name='index'),
    path('weldings',views.weldings,name='weldings'),
       path('structural',views.structural,name='structural'),
       path('heavy',views.heavy,name='heavy'),
       path('enquiry',views.enquiry,name='enquiry'),
       path('brass',views.brass,name='brass'),
] 
