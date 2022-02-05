import requests
import webbrowser

DATE = input("Enter Date(YYYYMMDD): ")
QTY = input("How many HOURS did you work this particular day: ")

#Opening up json file ------------------------------------------------
import json
  
with open('data.json', 'r') as openfile:
  
    # Reading from json file
    json_object = json.load(openfile)
  
USERNAME = json_object['username']
TOKEN = json_object["token"]

GRAPH_NAME = json_object["graph_name"]
GRAPH_ID = json_object["graph_id"]




# Posting a pixal ----------------------------------------------------------------

r_header = {
    'X-USER-TOKEN' : TOKEN
}

r_body = {             #request_body
    "date":f"{DATE}",
    "quantity": f"{QTY}",
}

response = requests.post(f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_NAME}", headers=r_header, json=r_body)
print(f"\n\nSent to Cloud, Status: {response.json()['message']}")

webbrowser.open(f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_NAME}.html")
exit = input("Press any key to exit")