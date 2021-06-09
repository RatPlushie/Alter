from django.shortcuts import render
from psd_tools import PSDImage

import base64
from io import BytesIO

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
    PIL_img = psd.composite()


    buffer = BytesIO()
    PIL_img.save(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    img = base64.b64encode(image_png)
    img = img.decode('utf-8')
    buffer.close()

    

    # Context dictionary for passing variable to HTML templates
    context = {'img_file': img}

    return render(request, 'alter_app/editor.html', context)