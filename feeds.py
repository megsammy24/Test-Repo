#!/usr/bin/env python
#Authors: Anastasia Bourlas and Megan Samuelson
from datetime import datetime
from stix.utils import idgen
import stix2
import cgi
import cgitb; cgitb.enable()
import pypyodbc

LABELS=["Cyber Security", "CTI", "Malicious Activity"] # Labels used for indicators

# Constant relationship for course-of-action and attack pattern
identity1 = stix2.Identity(
    id = "identity1",
    created = "",
    modified = str(datetime.now()),
    name = "Chemical Abstracts Service",
    identity_class = "organization",
    labels = ["Cyber Security", "CAS"],
    contact_information = "") # Provide our contact information
attackPattern1 = stix2.AttackPattern(
    id = "attack-pattern1", # Unique i.d. that identifies the object
    created = "", # The time at which the first version of the object was created
    modified = str(datetime.now()), # The time at which this version of the object was created
    name = "Compromised Account")
courseOfAction1 = stix2.CourseOfAction(
    id = "course-of-action1", # Unique i.d. that identifies the object
    created = "",
    modified = str(datetime.now()),
    name="Compromised Account",
    description="You may want to reset the password of the Compromised Account.")
# Constant Marking Definition that defines the TLP color
markingDefinition1 = stix2.MarkingDefinition(
    id = "marking-definition1", # Unique i.d. that identifies the object
    created = "",
    modified = str(datetime.now()),
    definition_type = "tlp",
    definition = {"tlp" : "amber"} )

relationship1 = stix2.Relationship(courseOfAction1, 'mitigates', attackPattern1) # Relationship between COA and Attack Pattern

def createJSONFile():
def createEmailAndSend():
    #This will need helper methods#########
    # pull an email from DB
    # if it's under alert only
        #don't attach JSON File
    #Else
    #Make Create JSON file and attach it to email

# Gets data from the form
def grabFormData():
    # Create instance of FieldStorage
    form = cgi.FieldStorage()
    # Get data from fields
    if form.getvalue('ip_addr_m'):
        text_content1 = form.getvalue('ip_addr_m')
   # Get data from fields
    if form.getvalue('time'):
       text_content2 = form.getvalue('time')
    print text_context1
    print text_context2

# Adds data to the database
def addToDB():
    connect = pypyodbc.connect('Driver={Sql Server Native Client 11.0};Server=.;Database=SAMPLE;Trusted_Connection=yes;')
    cursor = connect.cursor()
    print('Trying to insert!')
    cursor.execute("insert into [SAMPLE].[dbo].[Register] VALUES ('behzad','razzaqi')")
    connect.commit()
    print('Insert Finish!')
    connect.close()

#Adds each University as an identity
def addIdentity():
    identity2 = stix2.Identity(
        id = "identity2",
        created = "", modified = str(datetime.now()),
        name = "", #University name
        identity_class = "University",
        labels = ["Cyber Security"],
        contact_information = "datasec@cas.org") # Contact Info of the University


def addRelationshipIndicator_AttackPattern():
    # Relationship that connects indicator with attack pattern
    relationship2 = stix2.Relationship(addIndicator(), 'indicates', attackPattern1)


def addIndicator():
    indicator1 = Indicator(
        id = "indicator1", created = "", modified = str(datetime.now()),
		labels = LABELS,
        name = "IP Address of threat actor",
        description = "This IP Address has been shown to have malicious activity in gaining access through University accounts",
		pattern = "[ipv4-addr:value = '1.2.3.4']",
        valid_from = str(datetime.now()) )
        return indicator1
    relationship2 = stix2.Relationship(addIndicator(), 'indicates', addAttackPattern())

def addAttackPattern():
    attackPattern2 = stix2.AttackPattern(
        id = "attack-pattern2", # Unique i.d. that identifies the object
        created = "", # The time at which the first version of the object was created
        modified = str(datetime.now()), # The time at which this version of the object was created
        name = "Compromised Account")
    return attackPattern2

def initialize():

def addRelationship():
    relationship2 = stix2.Relationship(addIndicator(), 'indicates', addAttackPattern())

def addSighting():
    # Sighting of a malicious IP from a University
    sighting1 = Sighting(
        id = "sighting1", created = "", modified = str(datetime.now()),
        sighting_of_ref = "indicator1", # Will be the id of the indicator/IP they saw
        first_seen = "", # Timestamp of when Univ first saw the indicator
        last_seen = "") # Timestamp of the most recent encounter with the indicator

def main()
    grabFormData()
    print form
    addRelationship() # Call the addRelationship function
    addSighting() # Call the addSighting function
    addIdentity() # Call the addIdentity function
	bundle = stix2.Bundle(objects=[indicator1, identity1, identity2, sighting1, courseOfAction1, attackPattern1, attackPattern2, markingDefinition1,relationship1, relationship2, ]) # Bundles the objects together
	print bundle # Print out the bundle

#Call the main function
main()
