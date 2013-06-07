#!/usr/bin/env python

from database import db_session, init_db
from models import User
from forms import UserForm
from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


@app.route('/')
def show_entries():
    users = User.query.all()
    return render_template('show_entries.html', users=users)


@app.route('/delete/<id>')
def delete_page(id):
    user = User.query.filter(User.id == id).first()
    db_session.delete(user)
    db_session.commit()
    flash('Thanks for registering')
    return redirect(url_for('show_entries'))


@app.route('/edit/<id>',  methods=['GET', 'POST'])
def edit_page(id):
    print id
    user = User.query.filter(User.id == id).first()
    form = UserForm(request.form)
    if request.method == 'POST' and form.validate():
        #user = User(form.username.data, form.email.data)
        user.name = form.username.data
        user.email = form.email.data
        #user.update(dict(name=form.username.data, email=form.email.data))
        db_session.commit()
        flash('Thanks for registering')
        return redirect(url_for('show_entries'))
    form = UserForm(request.form, username=user.name, email=user.email)
    #user = User(form.username.data=user.name, form.email.data=user.email)
    return render_template('edit_page.html', form=form, id=user.id)


@app.route('/add',  methods=['GET', 'POST'])
def add_user():
    form = UserForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data)
        db_session.add(user)
        db_session.commit()
        flash('Thanks for registering')
        return redirect(url_for('show_entries'))
    return render_template('register.html', form=form)


@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    init_db()
    app.debug = True
    app.run()
