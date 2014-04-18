#!/usr/bin/python
import api
import pprint
import sys

# Get the data
baseURL = "http://us.battle.net/api/d3/profile/"
if len(sys.argv) > 1:
	username = sys.argv[1]#"MadMonkey" #HebrewHammer
	u_number = sys.argv[2]#"1157" #1601
else:
	username = "HebrewHammer"
	u_number = "1601"
profileURL = "%s%s-%s/" % (baseURL, username, u_number)
print profileURL #print out the target url
profileData, lastMod = api.call(url=profileURL, return_type = "JSON")

# Print it out

print type(profileData)
#print profileData
print type(lastMod)
print lastMod

#UNCOMMENT THE TWO FOLLOWING LINES TO PRINT PRETTY
pp = pprint.PrettyPrinter(indent=1)
pp.pprint(profileData)

print type(profileData)
heroes = (profileData["heroes"])
print heroes
for item in heroes:
	print "%s\t\t%s\t\t%s" % (item["name"], item["level"], item["class"])