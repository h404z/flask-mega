#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2019/10/5
# @Author: h404z

from flask import Flask
from config import Config

# 插件都在这里创建并初始化
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = "login"  # Flask-Login需要知道处理登录的视图函数是什么

from app import routes, models

if __name__ == '__main__':
    pass
