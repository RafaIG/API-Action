import os

SECRET_KEY = 'this is the secret key EGG&RIG'
PWD = os.path.abspath(os.curdir)
DEBUG = True
CORS_HEADERS = 'Content-Type'


MONGO_URI = 'mongodb://192.168.123.245:27017/observation'
#MONGO_URI = 'mongodb://localhost:27017/observation'


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'jpe', 'gif', 'jfif', 'jif', 'jfi', 'tiff', 'tiff', 'psd', 'pdf', 'eps', 'ai', 'indd', 'raw', 'svg', 'heif', 'webp'])
UPLOAD_FOLDER='img/'
