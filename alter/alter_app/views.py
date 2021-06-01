from django.shortcuts import render
from psd_tools import PSDImage

# Create your views here.
def index(request):
    return render(request, 'alter_app/index.html')


def upload(request):
    return render(request, 'alter_app/upload.html')


def login(request):
    return render(request, 'alter_app/login.html')


def gallery(request):
    return render(request, 'alter_app/gallery.html')


def editor(request):
    # Extrapolating the PSD to a PIL.Image
    psd = PSDImage.open('/mnt/Skryre/Users/Aki/Documents/Projects/Programs/Python/Alter/alter/static/psd/Customizable Synx Base.psd')
    image = psd.composite()

    

    # Context dictionary for passing variable to HTML templates
    context = {'img_file': image}

    return render(request, 'alter_app/editor.html', context)