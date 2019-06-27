from django.shortcuts import render

def render_game(request):
    
    return render(request, 'brick_breaker.html')
