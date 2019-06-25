from django.shortcuts import render

def display_dashboard(request):
    
    return render(request, 'dashboard.html')