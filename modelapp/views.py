from django.shortcuts import render

# Create your views here.

def Shopage(request):
    return render(request, "client.html")
