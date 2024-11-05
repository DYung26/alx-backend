#!/usr/bin/env python3
"""
This module initializes a Flask web application with Babel for
internationalization and localization support.

It configures the application to support English and French languages, and sets
the default timezone to UTC.
"""
from flask import Flask
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Configuration class for setting up application variables.

    Attributes:
        LANGUAGES (list): Supported languages for the application.
        TIMEZONE (str): Default timezone for the application.
    """
    LANGUAGES = ["en", "fr"]


app.config.from_object(Config)
app.config['BABEL_DEFAULT_LOCALE'] = Config.LANGUAGES[0]
app.config['BABEL_DEFAULT_TIMEZONE'] = "UTC"

if __name__ == "__main__":
    """
    Run the Flask application in debug mode when this script is executed
    directly.
    """
    app.run(debug=True)
