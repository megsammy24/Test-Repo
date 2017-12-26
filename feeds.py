#!/usr/bin/env python
#Authors: Anastasia Bourlas and Megan Samuelson
from datetime import datetime
import uuid
import stix2
import cgi, cgitb

def addAttackPattern():
    attackPattern2 = stix2.AttackPattern(created = str(datetime.now()),modified = str(datetime.now()),name = "Compromised Account")
    return attackPattern2

def main():
    AP = addAttackPattern()
    bundle = stix2.Bundle(objects=[AP])
    print bundle

# def grabFormData():
    # Create instance of FieldStorage
#form = cgi.FieldStorage()
#     # Get data from fields
#
# = form.getvalue('ip_addr_m')
# FORM_DATA.append(ip_addr_m) #FORM_DATA[0]
#
# if form.getvalue('time'):
#     time = form.getvalue('time')
#     FORM_DATA.append(time) #FORM_DATA[1]
#
# if form.getvalue('date'):
#     date = form.getvalue('date')
#     FORM_DATA.append(date) #FORM_DATA[2]
#
# if form.getvalue('hist'):
#     hist = form.getvalue('hist')
#     FORM_DATA.append(hist) #FORM_DATA[3]
#
# if form.getvalue('confirm'):
#     confirm = form.getvalue('confirm')
#     FORM_DATA.append(confirm) #FORM_DATA[4]

# print "Content-type:text/html; charset=utf-8\n\n"
# print "<html><head>"
# print "<title>My Webpage</title>"
# print "</head><body>"
# print "<h2> Selected Subject is %s</h2>" % ip_addr_m
# print "</body></html>"
