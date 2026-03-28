from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from .models import Report

def home(request):
    return render(request, 'reports/home.html')

def submit_report(request):
    if request.method == 'POST':
        report = Report(
        name=request.POST.get('name'),
        phone=request.POST.get('phone'),
        email=request.POST.get('email'),
        fault_type=request.POST.get('fault_type'),
        description=request.POST.get('description'),
        photo=request.FILES.get('photo'),
        address=request.POST.get('address'),
        latitude=request.POST.get('latitude') or None,
        longitude=request.POST.get('longitude') or None,
    )
        report.save()
        return render(request, 'reports/success.html', {'reference': report.reference_number})
    return render(request, 'reports/submit.html')

@staff_member_required
def admin_dashboard(request):
    reports = Report.objects.all().order_by('-submitted_at')
    return render(request, 'reports/admin_dashboard.html', {'reports': reports})

@staff_member_required
def update_status(request, reference_number):
    report = get_object_or_404(Report, reference_number=reference_number)
    if request.method == 'POST':
        report.status = request.POST.get('status')
        report.save()
        return redirect('admin_dashboard')
    return render(request, 'reports/update_status.html', {'report': report})


