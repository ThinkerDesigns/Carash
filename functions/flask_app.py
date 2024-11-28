import os
from flask import Flask, jsonify
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

# Import your Flask app from `app.py`
from app import app

# Create a WSGI application to work with Netlify Functions
def handler(event, context):
    return DispatcherMiddleware(app.wsgi_app, {
        '/api': app
    })
