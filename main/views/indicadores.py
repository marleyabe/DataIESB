from django.shortcuts import render

def indicadores(request):
    return render(request, 'indicadores.html')