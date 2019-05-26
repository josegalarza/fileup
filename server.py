#!/usr/bin/env python

import os
import random

from flask import Flask, request, redirect

# Config
HOST = "0.0.0.0"
PORT = 6666
DOC_FILE = 'doc.txt'
FILES_DIR = 'files'
INSTALL_FILE = 'install.sh'
CLEAN_SCRIPT = './clean.sh'

app = Flask(__name__)

@app.route('/')
@app.route('/help')
def help():
  with open(DOC_FILE) as f:
    return f.read(), 200

@app.route('/', methods=['POST'])
def post_file():
  try:
    file_data = request.files['file'].read()
    hash_code = '%032x' % random.getrandbits(128)
    with open(os.path.join(FILES_DIR, hash_code), 'wb') as f:
      #f = open(os.path.join(FILES_DIR, hash_code), 'wb')
      f.write(file_data)
      print('INFO Uploaded: %s' % hash_code)
      return '%s\n' % hash_code, 200
  except:
    help()

@app.route('/<hash_code>')
def get_file(hash_code):
  try:
    with open(os.path.join(FILES_DIR, hash_code)) as f:
      print('INFO Downloading: %s' % hash_code)
      return f.read(), 200
  except:
    print('ERROR Not found: %s' % hash_code)
    return '', 404

@app.route('/files')
def list_files():
  files = os.listdir(FILES_DIR)
  if files:
    return '%s\n' % '\n'.join(files), 200
  else:
    return '', 200

@app.route('/clean')
def clean_files():
  os.system(CLEAN_SCRIPT)
  return '', 200

@app.route('/install')
def install():
  with open(INSTALL_FILE) as f:
    return f.read(), 200

if __name__ == '__main__':
  try:
    os.mkdir(FILES_DIR)
  except:
    pass
  app.run(threaded=True, host=HOST, port=PORT)
