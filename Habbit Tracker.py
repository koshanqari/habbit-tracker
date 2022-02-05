import requests 
import datetime
import webbrowser

#datetime ---------------------------
today = datetime.datetime.now()
date_today = today.strftime("%Y%m%d")

#Opening up json file ------------------------------------------------
import json
  
with open('config\data.json', 'r') as openfile:
  
    # Reading from json file
    json_object = json.load(openfile)
  
USERNAME = json_object['username']
TOKEN = json_object["token"]

GRAPH_NAME = json_object["graph_name"]
GRAPH_ID = json_object["graph_id"]



#Ascii Art ---------------------------
print(
    '''
 _           _     _     _ _   
| |         | |   | |   (_) |  
| |__   __ _| |__ | |__  _| |_ 
| '_ \ / _` | '_ \| '_ \| | __|
| | | | (_| | |_) | |_) | | |_ 
|_| |_|\__,_|_.__/|_.__/|_|\__|'''
)

print("----------------------------------\n\n")


#App starts ------------------>>>>
def app():

    time = int(input("How many MINUTES did you Work ?: "))
    time = time/60


    # Getting back a pixal -------------------------------------------------

    r_header = {
        'X-USER-TOKEN' : 'thisissecret'
    }

    response = requests.get(f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_NAME}/{date_today}", headers=r_header)
    try:
        qty = float(response.json()["quantity"])
    except KeyError:
        qty = 0

    qty = qty + time 
    qty1 = "{:.2f}".format(qty) 

    print(f"Today you have Worked for: {qty1} hours")


    #Posting a pixal ----------------------------------------------------------------
    r_header = {
        'X-USER-TOKEN' : 'thisissecret'
    }

    r_body = {             #request_body
        "date":f"{date_today}",
        "quantity": f"{qty}",
    }

    response = requests.post(f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_NAME}", headers=r_header, json=r_body)
    print(f"\n\nSent to Cloud, Status: {response.json()['message']}")

    

loop = True
while loop:
    #Input/ Output ------------------>>>
    start = input("Update today or View Graph(u/v): ")
    if start == "v":
        webbrowser.open(f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_NAME}.html")
    else:
        app()