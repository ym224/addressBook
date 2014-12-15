import addressBookEntry
import json



def searchName(name):
    results=[]
    f = open("addressBook.json", "r")
    data = json.load(f)
    dataSize = len(data["entries"])
    for i in range(dataSize):
        if (name == data["entries"][i]["lastName"]):
            results.append(data["entries"][i])
    formatResults(results)

def formatResults(results):
    if not results:
        print ("No entry with name found in address book")
    else:
        for i in results:
            print "first name: " + str(i["firstName"])
            print "last name: " + str(i["lastName"])
            print "address: " + str(i["address"])
            print "city: " + str(i["city"])
            print "state: " + str(i["state"])
            print "zip code: " + str(i["zipCode"])
            print "phone number "+ str(i["phoneNumber"])            
            
        
    
search_input = raw_input("Please enter a last name to search: ")
searchName(search_input)

