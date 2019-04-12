from flask import Flask

UPLOAD_FOLDER = '/home/philipp/Downloads'

app = Flask(__name__, static_url_path='/test')
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
