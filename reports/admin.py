from django.contrib import admin
from .models import Report

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['reference_number', 'name', 'fault_type', 'status', 'submitted_at']
    list_filter = ['status', 'fault_type']
    search_fields = ['reference_number', 'name', 'phone']
    readonly_fields = ['reference_number', 'submitted_at', 'updated_at']
