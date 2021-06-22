from psd_tools import PSDImage
from io import BytesIO
import base64

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
    layer_list = reversed(list(img_location))

    return layer_list