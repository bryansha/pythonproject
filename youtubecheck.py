import json
import time
   
with open("list.json", encoding="utf8") as jsonFile:
    data = json.load(jsonFile)
    jsonFile.close()


def search():
    print("Enter the keyword: ")
    keyword = input()
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
    print("Enter your command: ")
    command = input()
    if (command == "search"):
        search()
    else:
        go = False
