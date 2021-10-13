# merakiAPProvisioner
#
#This bulk AP provisioner was built to speed up the deployment of new Meraki MR APs.
#
#The data source is a CSV file. It's built out in Excel with a column of the desired AP names beforehand. When the APs arrive on site, the serials can be scanned in the second column.
#
#In the inaugural run, I was able to prep ~30 new APs for deployment in about ten minutes and our install crew had them installed within the hour.
#
#The only manual piece to this process was applying the licensing, which wasn't too time consuming.
#
#The first payload moves the APs from inventory to the target network. The second renames the APs.
#
#As always, protect data like your API key and org ID and fold that into the script however you best see fit.
#
#-MS
