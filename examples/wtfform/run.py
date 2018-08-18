#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import OrderedDict
from flask import Flask, render_template, request
from wtforms import fields, validators
from wtforms.csrf.core import CSRFTokenField
from flask_wtf import FlaskForm

app = Flask("simple_form")
app.config.update(dict(SECRET_KEY="U7c*ky3Fed@9p"))


class MyForm(FlaskForm):
    int_field = fields.IntegerField(
        "int_field",
        validators=[
            validators.NumberRange(0, 9, message="Value is from 0 - 9!")]
    )
    str_field = fields.StringField(
        "str_field",
        validators=[
            validators.Length(0, 32, message="Length has to be shorter than 32 characters")
        ]
    )
    date_field = fields.DateField("date_field")
    textarea_field = fields.TextAreaField("textarea_field")
    ratio_field = fields.RadioField(
        "ratio_field",
        choices=[("a", "A"), ("b", "B"), ("c", "C")]
    )
    multi_select = fields.SelectMultipleField(
        "multi_select",
        choices=[("cpp", "C++"), ("py", "Python"), ("java", "Java")]
    )
    submit = fields.SubmitField('Submit')

    # def to_generic_data(self):
    #     for name, fields in self._fields:
    #         name, fields

    @property
    def generic_fields(self):
        if getattr(self, "_generic_fields", None) is None:
            _generic_fields = list()
            for name, field in self._fields.items():
                if not isinstance(field, (fields.SubmitField, CSRFTokenField)):
                    _generic_fields.append(name)
            self._generic_fields = _generic_fields
        return self._generic_fields

    def to_generic_data(self):
        return OrderedDict([
            (name, getattr(self, name).data)
            for name in self.generic_fields
        ])


@app.route('/submit', methods=('GET', 'POST'))
def submit():
    form = MyForm(request.form)
    if request.method == "POST" and form.validate_on_submit():
        data = form.to_generic_data()
        return str(data)

    return render_template('submit.html', form=form)


if __name__ == "__main__":
    """
    """

    app.run(debug=True)
