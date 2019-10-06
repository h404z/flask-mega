#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2019/10/5
# @Author: h404z

from flask import Flask

app = Flask(__name__)

from app import routes

if __name__ == '__main__':
    pass
