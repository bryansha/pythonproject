import json
import time
   
with open("list.json", encoding="utf8") as jsonFile:
    data = json.load(jsonFile)
    jsonFile.close()

def listall():
    for i in data:
        print(i['title'])
def search():
    keyword = input("Enter the keyword: ")
    starttime = time.time()
    countsearch = 0
    for i in data:
        if (keyword) in i["title"].lower():
            countsearch = countsearch +1
            
    endtime = time.time()    
    print(keyword + " appeared " + str(countsearch) + " times")        
    print("Took " + str(endtime-starttime) + " seconds")

go = True
while (go):
    command = input("Enter your command: ")
    if (command == "search"):
        search()
    elif (command == "listall"):
        listall()
    else:
        go = False