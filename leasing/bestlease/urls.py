from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('adminlogin/', views.adminlogin),
    path('register/', views.registerpage),
    path('approved/', views.approved),
    path('pending/', views.pending),
    path('uploadfile/<str:username>/', views.uploadfile),
    path('userlogin/', views.userlogin),
    path('viewimage/<str:username>/', views.viewimage),
    path('lessor/', views.lessorregister),
    path('lessorlogin/', views.lessorlogin),
    path('approve/<int:id>/', views.approve),
    path('logout/', views.logout),
    path('business/', views.businesspage),
    path('myupload/<str:username>/', views.myupload),
    path('user/', views.userpage),
    path('container/<int:id>/', views.container),
    path('book/', views.book),
    path('viewcontainer/', views.containerview),
    path('about/', views.about),
    path('order/<str:username>/', views.order),
]