#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
- How to: http://flask.pocoo.org/docs/0.12/quickstart/#file-uploads
- Patterns: http://flask.pocoo.org/docs/0.12/patterns/fileuploads/
"""

from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['csv_data']
        new_filename = secure_filename(f.filename)
        if new_filename == f.filename:
            dst = 'uploads/%s' % secure_filename(f.filename)
            f.save(dst)
            return "Success!"
        else:
            return "Your file name <strong>%s</strong> is invalid!" % f.filename


if __name__ == "__main__":
    """
    """
    app.run(debug=True)
