"""
URL configuration for bmsBackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('stations/', views.create_station),
    path('stations/all/', views.get_all_stations),
    path('stations/<int:id>', views.update_station),

    path('journey/', views.create_journey),
    path('get_journey/<int:id>', views.get_journey),
    path('journey/<int:id>', views.update_journey),
    path('end_journey/<int:id>', views.end_journey),
    
    
    path('journey_analytics/', views.get_journey_analytics),
    path('overall_analytics/', views.overall_analytics),
    
    
]

