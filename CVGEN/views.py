from django.shortcuts import render

def template1(request):
    return render(request, 'template1.html', {})

def template2(request):
    return render(request, 'template2.html')