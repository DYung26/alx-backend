#!/usr/bin/env python3
"""
This module starts a simple Flask web application that renders an HTML file.
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """
    Renders the home page of the web application.

    This function handles the root URL ('/') of the web application and
    returns the content of '0-index.html', which should be located in the
    'templates' folder.

    Returns:
        The rendered HTML page '0-index.html' as a response to the client.
    """
    return render_template('0-index.html')

if __name__ == '__main__':
    """
    Starts the Flask web server in debug mode if this script is run directly.

    When the script is executed as the main program, Flask's development
    server is launched on the default local server (http://127.0.0.1:5000).
    """
    app.run(debug=True)
