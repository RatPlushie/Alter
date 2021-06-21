from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from .models import Species

# TODO move these imports and the respective code to its on .py file to clean up the page
from psd_tools import PSDImage
from io import BytesIO
import base64

# Create your views here.
# Home Page
def index(request):
    return render(request, 'alter_app/index.html')


# Upload Page
@login_required(login_url='login')
def upload(request):
    # Querying DB for existing species
    species_list = Species.objects.all().order_by('name')

    # Passing context to renderer
    context = {'species_list': species_list}

    # Rendering page out
    return render(request, 'alter_app/upload.html', context)


# Login Page
def login_page(request):
    # Awaiting a post call from the request
    if request.method == 'POST':
        # Gathering username and password from the form
        username = request.POST.get('LoginUsername')
        password = request.POST.get('LoginPassword')

        # Django user authentication, will return "None" if unsuccessful
        user = authenticate(request, username=username, password=password)

        # Check if valid user
        if user is not None:
            # Django call to login in user
            login(request, user)

            # TODO redirect user to home page after successful login
        else:
            # When no valid user is found display a message prompt
            messages.info(request, 'Username or password invalid')

    # Passing context to renderer
    context = {}

    # Rendering page out
    return render(request, 'alter_app/login.html', context)


# Logout call
def logout_user(request):
    # Calling the django auth method for logging out a user
    logout(request)

    # Returning the user to the home page
    return redirect('home')


# Registartion Page
def registration(request):
    # Initialisation of registration form
    user_creation_form = RegistrationForm()

    # Awaiting request to create a new user
    if request.method == 'POST':
        # Init custom registration form from forms.py
        user_creation_form = RegistrationForm(request.POST)

        # Form validation
        if user_creation_form.is_valid():
            # If valid then save the user in the DB
            user_creation_form.save()

            # Creating a popup message when successful creation occurs
            user = user_creation_form.cleaned_data.get('username')
            messages.success(request, user + '\'s account successfully created')

            # redirect to login page on successful account creation
            return redirect('login_page')

        else:
            # TODO write error messages for invalid registrations
            pass

    # Passing context to renderer
    context = {'user_creation_form': user_creation_form}

    # Rendering page out
    return render(request, 'alter_app/registration.html', context)


# Gallery Page
def gallery(request):
    # Rendering page out
    return render(request, 'alter_app/gallery.html')


# PSD Editor Page
@login_required(login_url='login')
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

    # Rendering page out
    return render(request, 'alter_app/editor.html', context)