#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2019/10/8 20:17
# @Author: h404z
import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRETE_KEY') or 'you-are-beautiful'