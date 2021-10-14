# merakiAPProvisioner
#
#This bulk AP provisioner was built to speed up the deployment of new Meraki MR APs.
#
#It's named Starboy because I was listening to The Weeknd while writing it.
#
#I know there's a Meraki library, but I haven't played around with it yet. At the time of writing this script I just wanted to write based on what I knew.
#
#The data source is a CSV file. It's built out in Excel with a column of the desired AP names beforehand. When the APs arrive on site, the serials can be scanned in the second column. In this version of the script we use the values name, serial, tag, address, and notes.
#
#In the inaugural run, I was able to prep ~30 new APs for deployment in about ten minutes and our install crew had them installed within the hour.
#
#The only manual piece to this process was applying the licensing, which wasn't too time consuming.
#
#The first payload moves the APs from inventory to the target network. The second renames the APs and sets the other parameters that would be time-consuming to set manually through the Meraki Dashboard.
#
#As always, protect data like your API key and org ID and fold that into the script however you best see fit.
#
#-MS
