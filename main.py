import os

from config import *
from flask import Flask, redirect, url_for, render_template

server = Flask(__name__)

@server.route('/')
def start():
    return redirect(url_for('mainpage'))

@server.route('/mainpage', methods=['GET'])
def mainpage():
    return render_template('mainpage.html')

if __name__ == '__main__':
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))