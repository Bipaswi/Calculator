# Python parser for OpenMath (http://www.openmath.org/)
# See https://docs.python.org/3.4/library/xml.etree.elementtree.html

import xml.etree.ElementTree as ET
Element = ET.Element
SubElement = ET.SubElement

import omparse
from omparse import *

import omput
from omput import *

import error
from error import *

from xml.dom.minidom import *

import socket
import sys

################################################################

def ParseOMstring(omstring):
    root = ET.fromstring(omstring)
    omobj = ParseOMroot(root)
    return omobj

################################################################
#
# Variables for sending data over sockets, change as neccesary
#

HOST = 'localhost'
PORT = '43522'
s = None

################################################################

def OpenSocket():
    for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
        af, socktype, proto, canonname, sa = res

        try:
            s = socket.socket(af, socktype, proto)
        except socket.error as msg:
            s = None
            continue
        try:
            s.bind(sa)
            s.listen(1)
        except socket.error as msg:
            s.close()
            s = None
            continue
        break

    if s is None:
        print('Could not open socket')
        sys.exit(1)

    while True:
        print("Waiting for connect")
        conn, addr = s.accept()
        print('Connected by', addr)
        # Recieves data and sends back the exprssion
        while 1:
            data = conn.recv(1024)
            if not data: break
            try:
                normalObject = ParseOMstring(bytes.decode(data))
                conn.send(str.encode(bytes.decode(ET.tostring(OMobject(normalObject)))))

            except xml.etree.ElementTree.ParseError:
                conn.send(str.encode("Error in parse tree"))

            except TypeError:
                conn.send(str.encode("Cannot encode type"))

        conn.close()

################################################################

OpenSocket()
