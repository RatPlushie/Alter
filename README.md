# Alter
*This project is still being developed, thank you for your patience*

A new platform to upload and manage character templates.
Artists will be able to upload, store, and manage their creations. By uploading their .psd files and configuring them in-browser. Alter will be able to supply users wishing to make a character from the predefined templates' options. All without exposing the raw .psd files to the public, whilst avoiding the confusion that may come from newcomers to either your way of creation or the general image editing process.

## Features
- Template hosting
- Template configuration and extrapolation
- Colour mask generation (if required)
- .png/.jpeg exporting

## Technical
For security reasons sensitive information has been decoupled from the project. You will have to complete an .env file in the root directory for this to work. I have provided a blank backup of the .env file you can use.

```
SECRET_KEY=
DEBUG=
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
```

It is currently set up to accept MariaDB databases, though this is also configurable.

You will also have to import several PIPs
```
Django
django-storages
mysqlclient
Pillow
psd-tools
python-decouple
pylint-django
```
