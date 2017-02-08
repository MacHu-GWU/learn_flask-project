#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template

goodbye = Blueprint("goodbye", __name__, template_folder="templates")


@goodbye.route("/goodbye")
def say_goodbye():
    return render_template("index.html")


#--- Test ---
if __name__ == "__main__":
    from flask import Flask

    app = Flask("app")
    app.register_blueprint(goodbye)
    app.run(debug=True)
