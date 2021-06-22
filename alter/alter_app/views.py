from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from .models import Species, Art
from .utilities.image_control import *

# Create your views here.
# Home Page
def index(request):
    # Rendering page out
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

            # Returning the user to the home page
            return redirect('home')

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
            return redirect('login')

        else:
            # TODO write error messages for invalid registrations
            pass

    # Passing context to renderer
    context = {'user_creation_form': user_creation_form}

    # Rendering page out
    return render(request, 'alter_app/registration.html', context)


# Gallery Page
def gallery(request):
    # Getting all Art objects from DB
    art_list = Art.objects.all().order_by('species')

    # Getting a list of all art's storage locations
    location_list = list()
    for art in art_list:
        location_list.append(art.aws_location)
    
    # Converting each .psd file into base64 to be displayed in the gallery
    base64_img_list = list()
    for img in location_list:
        base64_img_list.append(get_img64(img))

    # Passing context to renderer
    context = {'img_list': base64_img_list}

    # Rendering page out
    return render(request, 'alter_app/gallery.html', context)


# FAQs Page
def faqs(request):
    #Rendering page out
    return render(request, 'alter_app/faqs.html')


# PSD Editor Page
@login_required(login_url='login')
def editor(request):
    # Returning a base64 image from a .psd
    img_location = '/mnt/Skryre/Users/Aki/Documents/Projects/Programs/Python/Alter/alter/static/psd/Customizable Synx Base.psd'
    base64_img = get_img64(img_location)

    # Storing the list of layers from the .psd file
    psd_layers = get_psd_layer_list(img_location)

    # Context dictionary for passing variable to HTML templates
    context = {
        'img_file': base64_img,
        'psd_layers': psd_layers,
    }

    # Rendering page out
    return render(request, 'alter_app/editor.html', context)