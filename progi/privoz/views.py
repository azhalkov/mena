from django.shortcuts import render


def privez(request):
    return render(request, 'privoz/privoz.html')