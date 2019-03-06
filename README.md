# fileup
File store web service

## Abstract

Fileup is a web service that can be used to upload/download files.

### How To Use

1. The user sends an HTTP request with the contents of a file to the web service.
2. The web service stores the file contents and associates it with an unique hashcode.
3. The web service returns a text response with an hash UR, which can be used to download the file.

```
$ curl "http://localhost:6666/" -F file=@file-to-upload
$ http://localhost:6666/h45hc0d3
```

### Server

```
# Clone repo
$ git clone git@github.com:josegalarza/fileup.git

# Run server
$ ./fileup/server.py
$ Fileup running in localhost:6666
```
