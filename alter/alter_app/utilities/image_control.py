from ..models import Art
from psd_tools import PSDImage
from PIL import Image
from io import BytesIO
import base64
import tempfile

class ArtBase:
	def __init__(self, art_ID):
		# Finding the art in the DB
		query = Art.objects.get(pk=art_ID)

		# Constructing the ArtBase object with the query result
		self.pk = query.pk
		self.title = query.title
		self.description = query.description
		self.author = query.author
		self.date = query.date
		self.psd_filename = query.psd_filename
		self.species = query.species.name
		
		# Building the other object elements
		#self.base64_img = get_img64(self.psd_filename)
		#self.psd_layers = get_psd_layer_list(self.psd_filename)

		# TODO retrieve or build the object's META file for the display of the .psd layers
		# TODO build thumbnail version of image // retreive the thumbnail from storage


class ArtLayer:
	def __init__(self, psd):
		# TODO write constructor for the creation of the list
		pass


def get_thumbnail(psd):
	# Pixel size of canvas
	THUMB_DIMENSIONS = (400, 400)

	# Getting file name
	file_name = str(psd).split('.')
	file_name = file_name[0]

	# Opening the PSD, converting to a PIL_img, resizing it to a smaller img
	psd = PSDImage.open(psd)
	pil_img = psd.composite()
	pil_img.thumbnail(THUMB_DIMENSIONS, Image.ANTIALIAS)

	# TODO Saving the manipulated thumbnail to a temporary location
	#pil_img.save()

	return pil_img

	
# Function to return a .png from a .psd file
def get_img64(psd_location):
	# Opening the .psd file
	psd = PSDImage.open(psd_location)

	# Extrapolating the PSD to a PIL.Image
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

	# Returning the .png image to the function call
	return img


def get_psd_layer_list(psd_location):
	# Opening the .psd file
	psd = PSDImage.open(psd_location)

	# Extracting a list of layers from the .psd file
	layer_list = reversed(list(psd))

	return layer_list


# Returning bool value after discovering what file extention is used
def is_psd(file_name):
	file_name_split = str(file_name).split('.')
	file_extention = file_name_split[-1]

	if file_extention == 'psd' or file_extention == 'PSD':
		return True

	else:
		return False