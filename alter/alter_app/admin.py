from django.contrib import admin
from .models import User, Species, Art

# Register your models here.
admin.site.register(Species)
admin.site.register(Art)