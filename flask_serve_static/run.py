#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This example explains how to serve static file from your local directory.

- Serve static file from local directory: http://flask.pocoo.org/docs/0.12/api/#flask.send_from_directory
- Handling URLs containing slash '/' character: http://flask.pocoo.org/snippets/76/
"""

from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/image/<path:filename>")
def serve_image(filename):
    return send_from_directory("image", filename)

if __name__ == "__main__":
    """
    """
    app.run(debug=True)