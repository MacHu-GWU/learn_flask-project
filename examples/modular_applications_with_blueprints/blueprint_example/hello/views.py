#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template

hello = Blueprint("hello", __name__, template_folder="templates")


@hello.route("/hello")
def say_hello():
    return render_template("index.html")


#--- Test ---
if __name__ == "__main__":
    from flask import Flask

    app = Flask("app")
    app.register_blueprint(hello)
    app.run(debug=True)
