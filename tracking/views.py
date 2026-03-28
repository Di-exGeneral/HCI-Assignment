from django.shortcuts import render, get_object_or_404, redirect
from reports.models import Report

def track_report(request):
    report = None
    error = None
    if request.method == 'POST':
        reference = request.POST.get('reference', '').strip().upper()
        try:
            report = Report.objects.get(reference_number=reference)
        except Report.DoesNotExist:
            error = 'No report found with that reference number. Please check and try again.'
    return render(request, 'tracking/track.html', {'report': report, 'error': error})

def cancel_report(request, reference_number):
    report = get_object_or_404(Report, reference_number=reference_number)
    if report.status != 'pending':
        return redirect('track_report')
    if request.method == 'POST':
        report.status = 'closed'
        report.save()
        return render(request, 'tracking/cancelled.html')
    return render(request, 'tracking/cancel_confirm.html', {'report': report})

def edit_report(request, reference_number):
    report = get_object_or_404(Report, reference_number=reference_number)
    if report.status != 'pending':
        return redirect('track_report')
    if request.method == 'POST':
        report.fault_type = request.POST.get('fault_type')
        report.description = request.POST.get('description')
        if request.FILES.get('photo'):
            report.photo = request.FILES.get('photo')
        report.save()
        return redirect('track_report')
    return render(request, 'tracking/edit_report.html', {'report': report})
