#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2019/10/6
# @Author: h404z

from app import app, db
from app.models import User, Posts


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User, "Posts": Posts}


if __name__ == '__main__':
    pass
