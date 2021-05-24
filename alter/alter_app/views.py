from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'alter_app/index.html')

def upload(request):
    return render(request, 'alter_app/upload.html')

def login(request):
    return render(request, 'alter_app/login.html')

def gallery(request):
    return render(request, 'alter_app/gallery.html')

