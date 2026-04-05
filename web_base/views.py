from django.shortcuts import render

def home(request):
    # Por ahora, solo le decimos que use un archivo llamado 'home.html'
    return render(request, 'home.html')