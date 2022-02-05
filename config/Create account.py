import requests
import json
import webbrowser


USERNAME = "some_username"
TOKEN = "thisissecret"

GRAPH_NAME = "some_graph"
GRAPH_ID = "some_graph"
UNIT = "hours"

#Creating a user ---------------------------------------

loop = True
while loop:
    USERNAME = input("enter your username (Small alphabet, no space or any other special characters): \n")
    TOKEN = "thisissecret"

    r_body = {             #request_body
        "token": TOKEN, 
        "username": USERNAME, 
        "agreeTermsOfService":"yes", 
        "notMinor":"yes"}

    response = requests.post("https://pixe.la/v1/users", json=r_body)

    print(response.json()['message'])
    if response.json()['message'][0] == "S":
        loop = False
        






#Creating a graph definition (making a graph) ---------------------------------
loop = True
while loop:

    GRAPH_NAME = input("enter Graph name (Small alphabet, no space or any other special characters): \n")
    GRAPH_ID = GRAPH_NAME
    r_header = {
        'X-USER-TOKEN' : TOKEN
    }

    r_body = {
        "id":GRAPH_ID,
        "name":GRAPH_NAME,
        "unit":UNIT,
        "type":"float",
        "color":"sora",
        "timezone": "Asia/Kolkata"
    }
    response = requests.post(f"https://pixe.la//v1/users/{USERNAME}/graphs", json=r_body, headers=r_header)

    print(response.json()['message'])
    if response.json()['message'][0] == "S":
        loop = False



json_data = {
    "username": USERNAME,
    "token": TOKEN,
    "graph_name": GRAPH_NAME,
    "graph_id" : GRAPH_ID, 
}
json_obj = json.dumps(json_data, indent=4)

with open("data.json", mode="w") as file:
    file.write(json_obj)

webbrowser.open(f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_NAME}.html")
exit = input("\n\nEnter any key to exit")