#!/usr/bin/env python

import os
import random

from flask import Flask, request, redirect

# Config
HOST = "localhost"
PORT = 6666

HELP = """API endpoints:
 GET  /            : Returns documentation
 POST /            : Uploads a file and returns its hash code. Use: curl URL -F file=@file-to-upload
 GET  /<hash_code> : Returns content from uploaded file related to the hash code
 GET  /files       : Returns list of files
 GET  /help        : Returns documentation
"""

app = Flask(__name__)

@app.route('/')
@app.route('/help')
def help():
  return HELP, 200

@app.route('/', methods=['POST'])
def post_file():
  try:
    hash_code = '%032x' % random.getrandbits(128)
    f = open(os.path.join('files', hash_code), 'wb')
    file_data = request.files['file'].read()
    f.write(file_data)
    f.close()
    print('INFO Uploaded: %s' % hash_code)
    return 'http://%s:%s/%s' % (HOST, PORT, hash_code), 200
  except Exception as e:
    return HELP, 200

@app.route('/<hash_code>')
def get_file(hash_code):
  try:
    f = open(os.path.join('files', hash_code))
    file_data = f.read()
    f.close()
    print('INFO Downloading: %s' % hash_code)
    return file_data, 200
  except Exception as e:
    print('ERROR Not found: %s' % hash_code)
    return '', 500

@app.route('/files')
def list_fles():
  return '\n'.join(os.listdir('files')), 200

if __name__ == '__main__':
  app.run(threaded=True, host=HOST, port=PORT)
