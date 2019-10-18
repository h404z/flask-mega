#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2019/10/6
# @Author: h404z

from app import app, db
from app.models import User, Posts


@app.shell_context_processor  # 当 flask shell 命令运行时，它将调用这个函数并在 shell 会话中注册它返回的项目
def make_shell_context():
    return {"db": db, "User": User, "Posts": Posts}


if __name__ == '__main__':
    pass
