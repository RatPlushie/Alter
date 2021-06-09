from django.shortcuts import render
from psd_tools import PSDImage
from io import BytesIO
import base64


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

    # Saving the PIL.Image as a .png file in a buffer
    buffer = BytesIO()
    PIL_img.save(buffer, format='png')
    buffer.seek(0)

    # Converting the buffer to a usable base64 format for display on the webpage
    image_png = buffer.getvalue()
    img = base64.b64encode(image_png)
    img = img.decode('utf-8')
    buffer.close()


    # Context dictionary for passing variable to HTML templates
    context = {'img_file': img}

    return render(request, 'alter_app/editor.html', context)