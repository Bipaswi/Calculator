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

################################################################

def ParseOMfile(fname):
    tree = ET.parse(fname)
    root = tree.getroot()
    omobj = ParseOMroot(root)
    return omobj

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

def OMstring(x):
    return ET.tostring(OMobject(x))

def OMprint(x):
    print(parseString(ET.tostring(OMobject(x))).toprettyxml(indent = "    "))

def OMSend(x):
    # Setting up connection to host
    for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
        af, socktype, proto, canonname, sa = res
        try:
            s = socket.socket(af, socktype, proto)
        except socket.error as msg:
            s = None
            continue
        try:
            s.connect(sa)
        except socket.error as msg:
            s.close()
            s = None
            continue
        break

    if s is None:
        print('Could not open socket')
        # Return open math error?
    else:
        print("Sending: ", x , '\n')
        s.sendall(str.encode(x))
        data = s.recv(1024)
        s.close()
        print('Received:', bytes.decode(data))

################################################################
