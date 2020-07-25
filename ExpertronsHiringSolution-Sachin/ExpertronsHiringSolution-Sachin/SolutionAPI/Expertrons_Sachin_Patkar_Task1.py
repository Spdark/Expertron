import pprint 
import requests 
secret = "3ad0d809d497497b86f01fafb73e4ebb"
print("1. Query")
print("2. Source")
print("3. Exit")
while(1):
    c = int(input("Choice any one option: "))
    title = input("Enter the Title: (Eg = Bitcoin)")
    if(c == 1):
        url = "http://newsapi.org/v2/everything?"
        p = {
            'q': title, 
            'pageSize': 10, 
            'apiKey': secret 
        } 
        s = requests.get(url,params = p) 
        page = s.json() 
        r = []
        for i in page['articles']:
            r.append(i['title'])
        for i in range(len(r)):
            print(i+1,r[i])        
    elif(c == 2):
        url = "https://newsapi.org/v2/top-headlines?"
        p = {
            'sources': title, 
            'pageSize': 10, 
            'apiKey': secret 
        }
        s = requests.get(url,params=p) 
        page = s.json() 
        r = []
        for i in page['articles']:
            r.append(i['title'])
        for i in range(len(r)):
            print(i+1,r[i])        
    else:
        exit(1)

