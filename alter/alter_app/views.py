from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm
from .models import Species
from psd_tools import PSDImage
from io import BytesIO
import base64

# Create your views here.
# Home Page
def index(request):
    return render(request, 'alter_app/index.html')


# Upload Page
def upload(request):
    # Querying DB for existing species
    species_list = Species.objects.all().order_by('name')

    # Passing context to renderer
    context = {'species_list': species_list}

    return render(request, 'alter_app/upload.html', context)


# Login Page
def login(request):
    # Initialising registration form
    user_creation_form = RegistrationForm()

    # Awaiting request to create a new user
    if request.method == 'POST':
        user_creation_form = RegistrationForm(request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            # Creating a popup message when successful creation occurs
            user = user_creation_form.cleaned_data.get('username')
            messages.success(request, user + '\'s account successfully created')

        else:
            # TODO write error messages for invalid registrations
            pass

    # Passing context to renderer
    context = {'user_creation_form': user_creation_form}

    return render(request, 'alter_app/login.html', context)


# Gallery Page
def gallery(request):
    return render(request, 'alter_app/gallery.html')


# PSD Editor Page
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

    # Getting an ordered list of layers from the PSD
    psd_structure = reversed(list(psd))

    # Context dictionary for passing variable to HTML templates
    context = {
        'img_file': img,
        'psd': psd_structure,
    }

    return render(request, 'alter_app/editor.html', context)