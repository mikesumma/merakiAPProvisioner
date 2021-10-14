import csv
import requests
import time

#Fill in your variables, convert this section to environmental variables, or alter the variables to be input.
#Whatever you want to do, always protect this information, especiall your Dashboard API key!
API_KEY = ""
org_id = ""
network = ""

#Declaration of variables, setting up URLs, prepping the action batch payloads.

baseURL = "https://api.meraki.com/api/v1"
moveURL = f"{baseURL}/networks/{network}/devices/claim"
moveAPs = []
renameURL = f"{baseURL}/organizations/{org_id}/actionBatches"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

movePayload = {
    "serials": moveAPs
}

renamePayload = {
    "confirmed": True,
    "synchronous": False,
    "actions": [
    ],
}

#Opens the CSV file. You need the following columns when building in a spreadsheet:
#Name, Serial, Tag, Address, Notes
#Of course this can be built out to whatever you'd like as long as it's within the schema.
#Name your CSV ap.csv and put it in the same directory as this script.
try:
    with open('ap.csv') as f:
        reader = csv.DictReader(f)
        apList = list(reader)
except:
    print("Error opening ap.csv. Wrong format or file not found.")

#I wanted to name this thing something and was listening to The Weeknd when I was creating this script.
print("***STARBOY*** BULK AP PROVISIONER is running...")
time.sleep(1)

#Runs through the CSV and appends to the action batches.
for line in apList:
    apName = line['name']
    apSerial = line['serial']
    apTag = line['tag']
    apAddress = line['address']
    apNotes = line['notes']
    moveAPs.append(apSerial)
    apConfig = {
            "resource": f"/devices/{apSerial}",
            "operation": "update",
            "body": {"name": apName,
            "address": apAddress,
            "notes": apNotes,
            "tags": [ apTag ]
            }
        }
    renamePayload['actions'].append(apConfig)

#The first POST moves the APs from inventory to your target network.
#A succesfull status code is 200
print("Moving APs...")
responseMove = requests.post(moveURL, json=movePayload, headers=headers)
code = (responseMove.status_code)
print("Status code is " + str(code))
time.sleep(1)

#The second POST sends the config parameters.
#A successful status code is 201
print("Sending rename and configuration payload...")
response = requests.post(renameURL, json=renamePayload, headers=headers)
code = (response.status_code)
print("Status code is " + str(code))
time.sleep(1)

print("***STARBOY*** complete.")