# -*- coding: utf-8 -*-

import os
import logging
import re

from app import app
from flask import render_template, request


@app.route('/')
@app.route('/index')
def index():
    return "HELLO, FLASK WORLD"

@app.route('/test')
def client():
    return render_template('index.html')

@app.route('/static')
def aaa():
    return app.send_static_file('index.html')
