#!/usr/bin/env python
#Authors: Anastasia Bourlas and Megan Samuelson
from datetime import datetime
import uuid
import cgi
import cgitb

# def grabFormData():
    # Create instance of FieldStorage
form = cgi.FieldStorage()
#     # Get data from fields
#
ip_addr_m = form.getvalue('ip_addr_m')
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

print "Content-type:text/html\r\n\r\n"
print "<html><head>"
print "<title>Radio - Fourth CGI Program</title>"
print "</head><body>"
print "<h2> Selected Subject is</h2>"
print "</body></html>"
