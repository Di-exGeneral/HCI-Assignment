from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('submit/', views.submit_report, name='submit_report'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('update-status/<str:reference_number>/', views.update_status, name='update_status'),
]
