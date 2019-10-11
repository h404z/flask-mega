#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2019/10/5
# @Author: h404z

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models

if __name__ == '__main__':
    pass
