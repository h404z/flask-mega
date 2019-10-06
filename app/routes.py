#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2019/10/6
# @Author: h404z
from flask import render_template
from app import app


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "NickHo"}
    return render_template("index.html", title="Home", user=user)


if __name__ == '__main__':
    pass
