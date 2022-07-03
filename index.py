# opencv-contrib-python-headless

from routes.camara import formatoVideo
from routes.templates import plantilla
from routes.cara2 import formatoVideoCara2
from routes.manos import formatoVideo3
from routes.cuerpos import formatoVideo4
# from routes.index import templateFile
from routes.fileProcess import processFile
from flask import Flask




def generate():
     app = Flask(__name__)
     app.register_blueprint(plantilla)
     app.register_blueprint(formatoVideo)
     app.register_blueprint(formatoVideoCara2)
     app.register_blueprint(formatoVideo3)
     app.register_blueprint(formatoVideo4)
     # app.register_blueprint(templateFile)
     app.register_blueprint(processFile)
     return app
if __name__ == "__main__":
     generate().run(debug=False)
