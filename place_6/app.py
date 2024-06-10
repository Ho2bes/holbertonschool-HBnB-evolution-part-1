#!/usr/bin/python3

from flask import Flask
from api import api_bp

app = Flask(__name__)
app.config['RESTPLUS_MASK_SWAGGER'] = False

# Enregistrer le Blueprint de l'API
app.register_blueprint(api_bp, url_prefix='/api')

if __name__ == "__main__":
    app.run(debug=True)
