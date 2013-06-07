#!/usr/bin/env python

from wtforms import Form, BooleanField, TextField, PasswordField, validators


class UserForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=25)])
    email = TextField('Email Address', [validators.Length(min=6, max=35)])
