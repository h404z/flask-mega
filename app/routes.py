#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2019/10/6
# @Author: h404z

from app import app


@app.route("/")
@app.route("/index")
def index():
    return "hello flask"


if __name__ == '__main__':
    pass
