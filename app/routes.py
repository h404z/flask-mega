#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2019/10/6
# @Author: h404z
from flask import render_template, redirect, flash, url_for
from flask_login import current_user, login_user, logout_user
from app import app
from app.forms import LoginForm
from app.models import User


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
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("login"))

        # 把用户注册为登录状态，意味着将来用户访问的任何页面都会将 current_user这个变量设置为这个用户
        login_user(user, remember=form.remember_me.data)

        return redirect(url_for("index"))  # url_for(函数名)
    return render_template("login.html", title="Sign In", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


if __name__ == '__main__':
    pass
