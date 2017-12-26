#!/usr/bin/env python
#Authors: Anastasia Bourlas and Megan Samuelson
from datetime import datetime
#import stix2
import uuid
import cgi
import cgitb; cgitb.enable()
#import pypyodbc
FORM_DATA = []
LABELS=["Cyber Security", "CTI", "Malicious Activity"] # Labels used for indicators

# Constant relationship for course-of-action and attack pattern
# identity1 = stix2.Identity(
#     created = "",
#     modified = str(datetime.now()),
#     name = "Chemical Abstracts Service",
#     identity_class = "organization",
#     labels = ["Cyber Security", "CAS"],
#     contact_information = "datasec@cas.org" )# Provide our contact information
#
# attackPattern1 = stix2.AttackPattern(
#     created = "",
#     modified = str(datetime.now()),
#     name = "Compromised Account")
# courseOfAction1 = stix2.CourseOfAction(
#     created = "",
#     modified = str(datetime.now()),
#     name="Compromised Account",
#     description="You may want to reset the password of the Compromised Account.")
#
# # Constant Marking Definition that defines the TLP color
# markingDefinition1 = stix2.MarkingDefinition(
#     created = "",
#     definition_type = "tlp",
#     definition = {"tlp" : "amber"})
#
# relationship1 = stix2.Relationship(courseOfAction1, 'mitigates', attackPattern1) # Relationship between COA and Attack Pattern

def grabFormData():
    # Create instance of FieldStorage
    form = cgi.FieldStorage()
    # Get data from fields
    if form.getvalue('ip_addr_m'):
        ip_addr_m = form.getvalue('ip_addr_m')
        FORM_DATA.append(ip_addr_m) #FORM_DATA[0]

    if form.getvalue('time'):
        time = form.getvalue('time')
        FORM_DATA.append(time) #FORM_DATA[1]

    if form.getvalue('date'):
        date = form.getvalue('date')
        FORM_DATA.append(date) #FORM_DATA[2]

    if form.getvalue('hist'):
        hist = form.getvalue('hist')
        FORM_DATA.append(hist) #FORM_DATA[3]

    if form.getvalue('confirm'):
        confirm = form.getvalue('confirm')
        FORM_DATA.append(confirm) #FORM_DATA[4]

# Adds data to the database
def addToDB():
    connect = pypyodbc.connect('Driver={Sql Server Native Client 11.0};Server=.;Database=SAMPLE;Trusted_Connection=yes;')
    cursor = connect.cursor()
    print 'Trying to insert!'
    cursor.execute("insert into [SAMPLE].[dbo].[Register] VALUES ('behzad','razzaqi')")
    connect.commit()
    print 'Insert Finish!'
    connect.close()

def createJSONFile():
    print 'Hey There'

# def addIdentity():
#     identity2 = stix2.Identity(
#     created = "",
#     modified = str(datetime.now()),
#     name = "",
#     identity_class = "University",
#     labels = ["Cyber Security"],
#     contact_information = "datasec@cas.org") # Contact Info of the University
# def addRelationship():
#     # Relationship that connects indicator with attack pattern
# 	relationship2 = stix2.Relationship(addIndicator(), 'indicates', attackPattern1)
#
# def addIndicator():
#     indicator = Indicator(
#     created = "",
#     modified = str(datetime.now()),
#     labels = LABELS,
#     name = "IP Address of threat actor",
#     description = "This IP Address has been shown to have malicious activity in gaining access through University accounts",
#     pattern = "[ipv4-addr:value = [FORM[0]]]",
#     valid_from = datetime.now() )
#     return indicator
# def addAttackPattern():
#     attackPattern2 = stix2.AttackPattern(
#     created = "",
#     modified = str(datetime.now()),
#     name = "Compromised Account")
#     return attackPattern2
#
# def addSighting():
#     # Sighting of a malicious IP from a University
#     sighting1 = Sighting(
#     created = "",
#     modified = str(datetime.now()),
#     sighting_of_ref = "indicator1",
#     first_seen = "",
#     last_seen = "") # Timestamp of the most recent encounter with the indicator

# def main():
#     print 'Hello World'
    #grabFormData()
    #addRelationship() # Call the addRelationship function
    #addSighting() # Call the addSighting function
    #addIdentity() # Call the addIdentity function
    #bundle = stix2.Bundle(objects=[ identity1, courseOfAction1,attackPattern1,  markingDefinition1, relationship1]) # Bundles the objects together
    #print bundle # Print out the bundle
#main()
