#!/usr/bin/python3

# Entry point for the Flask application

from api import app

if __name__ == "__main__":
    app.run(debug=True)
