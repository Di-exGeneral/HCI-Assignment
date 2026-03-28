from django.urls import path
from . import views

urlpatterns = [
    path('track/', views.track_report, name='track_report'),
    path('cancel/<str:reference_number>/', views.cancel_report, name='cancel_report'),
    path('edit/<str:reference_number>/', views.edit_report, name='edit_report'),
]




