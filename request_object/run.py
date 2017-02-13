#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ref: http://flask.pocoo.org/docs/0.12/quickstart/#the-request-object
"""

from flask import Flask, request, render_template
from pprint import pprint as ppt

app = Flask(__name__)

multiple_choice_options = ["Apple", "Banana", "Cherry", "Dragonfruit", "Grape"]


def get_defualt_kwargs():
    """
    """
    kwargs = {
        "multiple_choice_options": multiple_choice_options,
    }
    return kwargs


def get_form_data(req):
    """flask.request.form是werkzeug.datastructures.ImmutableMultiDict。
    
    1. 这种dict比较特殊, 内部其实是一个tuple的列表。并且对于同一个key, 可能有多个
    值: ``[("tag", "Apple"), ("tag", "Banana")]``。所以我们需要用:
    ``form.getlist(key)`` 方法来获得该项的数据。
    2. requests.form的数据的值永远都是字符串。因为前端技术中input的type只是限定
    了用户的输入, 但实际上本质上还是字符串。如果要将字符串转化成相应的app级数据,
    则推荐使用 `Flask_wtf <https://flask-wtf.readthedocs.io/en/stable/>`_。
    """
    # read form data
    form_data = dict()
    print(type(req.form))
    for key, value in req.form.items():
        value = value.strip()
        if value:
            form_data[key] = value
    form_data["multiple_choice"] = req.form.getlist("multiple_choice")
    
    return form_data


@app.route("/", methods=["GET", "POST"])
def index():
    """Homepage.
    """
    kwargs = get_defualt_kwargs()
    
    if request.method == "GET":
        return render_template("index.html", **kwargs)

    elif request.method == "POST":
        form_data = get_form_data(request)  # get form_data
        ppt(form_data)
        kwargs.update(form_data)
        return render_template("index.html", **kwargs)


if __name__ == "__main__":
    """
    """
    app.run(debug=True)
