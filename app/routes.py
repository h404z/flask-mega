#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2019/10/6
# @Author: h404z
from flask import render_template, redirect, flash, url_for
from app import app
from app.forms import LoginForm


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "NickHo"}

    posts = [
        {
            "author": {"username": "Vicky"},
            "body": "I want to go to Disneyland!"
        },
        {
            "author": {"username": "Hayden"},
            "body": "I'm a little human!"
        }
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login requested for user {}, remember me={}".format(form.username.data, form.remember_me.data))
        return redirect(url_for("index"))  # url_for(函数名)
    return render_template("login.html", title="Sign In", form=form)


if __name__ == '__main__':
    pass
