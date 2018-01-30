#!/usr/bin/env python

#import dependencies
import re
import socket
import argparse
import urllib.request


#function
def main(args):
  print("Hello world!")
  print(args)

main('Running main function')
 
#variables
host = '127.0.0.1'
port = 80

#socket connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))
sock.recv(1024)
sock.send(b'Hello world!')

#get request
urllib.request.urlopen("http://example.com/foo/bar").read()
