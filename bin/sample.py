#!/usr/bin/python
import api
import pprint
import sys

# Get the data
baseURL = "http://us.battle.net/api/d3/profile/"
username = sys.argv[1]#"MadMonkey" #HebrewHammer
u_number = sys.argv[2]#"1157" #1601
profileURL = "%s%s-%s/" % (baseURL, username, u_number)
print profileURL
profileData = api.call(url=profileURL, return_type = "JSON")

# Print it out
pp = pprint.PrettyPrinter(indent=1)
pp.pprint(profileData)


