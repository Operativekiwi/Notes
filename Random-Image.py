import os
import random
from flask import Flask, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Set the local storage location for images
IMAGE_FOLDER = 'C:\\Users\\GGPC\\Documents\\Projects\\Random-Images\\Images'

@app.route('/random-image')
def get_random_image():
    # Get a list of all the image files in the image folder
    image_files = [os.path.join(IMAGE_FOLDER, f) for f in os.listdir(IMAGE_FOLDER) if f.endswith('.jpg') or f.endswith('.png')]

    # Choose a random image file from the list
    image_file = random.choice(image_files)

    # Return the image file to the client
    return send_file(image_file, mimetype='image/jpg')

if __name__ == '__main__':
    app.run()
