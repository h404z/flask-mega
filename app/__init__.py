#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2019/10/5
# @Author: h404z

from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes

if __name__ == '__main__':
    pass
