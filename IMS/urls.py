"""
URL configuration for IMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from base.views import register,ProductTypeApiView,ProductApiView,ProductDetailApiView,PurchaseApiView,DepartmentApiView,VendorApiView,SalesApiView,CustomerApiView,login,group

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product-types/',ProductTypeApiView.as_view({'get':'list','post':'create'})),
    path('product-types/<int:pk>/',ProductTypeApiView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('products/',ProductApiView.as_view()),
    path('s/<int:pk>/',ProductDetailApiView.as_view()),
    path('purchase/',PurchaseApiView.as_view({'get':'list','post':'create'})),
    path('department/',DepartmentApiView.as_view({'get':'list','post':'create'})),
    path('department/<int:pk>/',DepartmentApiView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('vendor/',VendorApiView.as_view({'get':'list','post':'create'})),
    path('vendor/<int:pk>/',VendorApiView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('sales/',SalesApiView.as_view({'get':'list','post':'create'})),
    path('customer/',CustomerApiView.as_view({'get':'list','post':'create'})),
    path('register/',register),   
    path('login/',login), 
    path('groups/',group)
]
