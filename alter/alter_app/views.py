from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, UploadForm
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
    # Init upload form
    upload_form = UploadForm()

    # TODO write POST call
    if request.method == 'POST':
        pass

    # Querying DB for existing species
    species_list = Species.objects.all().order_by('name')

    # Passing context to renderer
    context = {
        'species_list': species_list,
        'upload_form': upload_form    
    }

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

    # Rendering page out
    return render(request, 'alter_app/login.html')



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
    # TODO Paginate the gallery onto several pages
    # TODO display thumbnails in production, not full sized images

    # Getting all Art objects from DB 
    art_list = Art.objects.all().order_by('species')

    # Creating a list of art objects to send to the template
    bases_list = list()
    for art in art_list:
        bases_list.append(ArtBase(art.pk))

    # Passing context to renderer
    context = {'bases_list': bases_list}

    # Rendering page out
    return render(request, 'alter_app/gallery.html', context)



# FAQs Page
def faqs(request):
    #Rendering page out
    return render(request, 'alter_app/faqs.html')



# PSD Editor Page
@login_required(login_url='login')
def editor(request, pk):
    # Creating the Artbase Object
    art_template = ArtBase(pk)

    # Context dictionary for passing variable to HTML templates
    context = {
        'img_file': art_template.base64_img,
        'psd_layers': art_template.psd_layers,
    }

    # Rendering page out
    return render(request, 'alter_app/editor.html', context)