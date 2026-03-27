from django.shortcuts import render

def submit_report(request):
    return render(request, 'reports/submit.html')


def home(request):
    return render(request, 'reports/home.html')

