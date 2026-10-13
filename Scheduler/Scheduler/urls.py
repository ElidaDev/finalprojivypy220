"""
URL configuration for Scheduler project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from ScheduleApp import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/',views.showEmployees, name="employees"),
    path('schedules/',views.showSchedules, name="showSchedules"),
    path('addshift/',views.AddShift, name="addShift"),
    path('addshiftevent/',views.AddShiftEvent, name="addShiftEvent"),
    path('<int:id>/editShift',views.EditShift, name="editShift"),
    path('<int:id>/editEvent',views.EditShiftEvent, name="editShiftEvent"),
    path('<int:id>/deleteEvent',views.deleteShiftEvent, name="deleteShiftEvent"),
    path('<int:id>/deleteShift',views.deleteShift, name="deleteShift"),
    path('dayview/<int:shiftId>/', views.dayView, name='shiftDayView'),
    path('',views.calendarView, name="schedule")
]
