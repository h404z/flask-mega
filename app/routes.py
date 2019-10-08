#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2019/10/6
# @Author: h404z
from flask import render_template
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

@app.route("/login")
def login():
    form = LoginForm()
    # todo: 表单接收功能未实现 https://github.com/Microndgt/The-Flask-Mega-Tutorial/blob/master/The-Flask-Mega-Tutorial/part3.md
    return render_template("login.html", title="Sign In", form=form)



if __name__ == '__main__':
    pass
