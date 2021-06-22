from ..models import Art
from psd_tools import PSDImage
from io import BytesIO
import base64

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
        self.aws_location = query.aws_location
        self.species = query.species.name
        
        # Building the other object elements
        self.base64_img = get_img64(self.aws_location)
        self.psd_layers = get_psd_layer_list(self.aws_location)

        # TODO retrieve or build the object's META file for the display of the .psd layers
        # TODO build thumbnail version of image // retreive the thumbnail from storage

    
# Function to return a .png from a .psd file
def get_img64(img_location):
    # Opening the .psd file
    psd = PSDImage.open(img_location)

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


def get_psd_layer_list(img_location):
    # Opening the .psd file
    psd = PSDImage.open(img_location)

    # Extracting a list of layers from the .psd file
    layer_list = reversed(list(psd))

    return layer_list