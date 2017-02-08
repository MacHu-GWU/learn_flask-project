#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask

def create_app():
    from flask_blue_print_example_app.hello import hello
    from flask_blue_print_example_app.goodbye import goodbye
    
    app = Flask("app")
    for bp in [hello, goodbye]:
        app.register_blueprint(bp)
    
    return app