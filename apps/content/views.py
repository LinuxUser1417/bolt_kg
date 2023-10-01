from django.shortcuts import render

def bolt_sales(request):
    return render(request, 'sales.html')
