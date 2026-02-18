from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'about.html')
def agents(request):
    return render(request, 'agents.html')
def contact(request):
    return render(request, 'contact.html')
def index(request):
    return render(request, 'index.html')
def properties(request):
    return render(request, 'properties.html')
def propertysingle(request):
    return render(request, 'propertysingle.html')
