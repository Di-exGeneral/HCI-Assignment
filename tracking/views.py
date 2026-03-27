from django.shortcuts import render


def track_report(request):
    return render(request, 'tracking/track.html')
