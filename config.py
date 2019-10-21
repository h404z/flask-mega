#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2019/10/8 20:17
# @Author: h404z
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRETE_KEY') or 'you-are-beautiful'

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 禁用不需要的Flask-SQLAlchemy功能，即每次在数据库中进行更改时都会向应用程序发出信号。
