#!/usr/bin/env python3
'''
BASED ON https://www.youtube.com/watch?v=ZHtamOF9ekg
Using DVWA Virtual Machine
'''
import requests
import sys
import urllib.parse

LOGIN_URL = "http://IP/login.php"
SEC_URL = "http://IP/security.php"
SQL_URL = "http://IP/vulnerabilities/sqli_blind/"

#Init a session
sesion = requests.session()

#1. LOGIN in order to maintain session cookies etc. with default DVWA credentials
def login(url):
    login_payload = dict(username='admin', password='password', Login='Login')
    sesion.post(format(url), login_payload)
    changeSecurity("low")
    #return sesion.cookies


#low, medium, high
def changeSecurity(secLevel):
    security_payload = dict(security=secLevel, seclev_submit='Submit')
    sesion.post(format(SEC_URL), security_payload)
