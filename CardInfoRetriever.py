import requests
import json
import csv


with open("cardRetrieverConfig.txt", "r") as file:
    content = file.readlines()
    playerTag = content[0].split("=")[1].strip()
    apiToken = content[1].split("=")[1].strip()

playerServicesEndpoint = 'players/%23' + playerTag


def makeCsvListFromCardEntry(entry, header):
    entryList = []
    for entryType in header:
        entryList.append(entry[entryType])
    return entryList
        

httpAddress = "https://api.clashroyale.com/v1/"+ playerServicesEndpoint;
authorization = "Bearer " + apiToken;
r=requests.get(httpAddress, headers={"Accept":"application/json", "authorization":authorization}, params = {"limit":200})
status = str(r.status_code)
if(status != '200'):
    result = "Server responded: "+ status + "! Can't retrieve card info..." 
else:
    result =  json.dumps(r.json(), indent = 2)
    resultDict = json.loads(result)["cards"]
    file = open('result.csv', 'w',  newline='')
    header= ['name', 'id', 'level', 'maxLevel', 'count'] 
    write = csv.writer(file)
    write.writerow(header) 
    for entry in resultDict:
        write.writerow(makeCsvListFromCardEntry(entry, header)) 
    file.close()
    result = "Data saved successfully to: " + file.name

print(result)

















