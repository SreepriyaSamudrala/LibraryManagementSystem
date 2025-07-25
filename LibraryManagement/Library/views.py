from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')
def addbook(request):
    return render(request, 'addbooks.html')

def viewbooks(request):
    return render(request, 'viewbooks.html')

def contactus(request):
    return render(request, 'contactus.html')

def aboutus(request):
    return render(request, 'aboutus.html')