import requests, os
from todo_item import Item

headers = {
   "Accept": "application/json"
}

def get_items():
    api_key = os.getenv("TRELLO_API_KEY")
    board_id = os.getenv("TRELLO_BOARD_ID")
    token = os.getenv("TRELLO_TOKEN")

    url = f"https://api.trello.com/1/boards/{board_id}/lists?key={api_key}&token={token}&cards=open"
    response = requests.request("GET", url, headers=headers).json() 
    items = []
    for list in response: 
        for item in list["cards"]:
            if item["closed"]:
                continue
            else:
                items.append(Item.fetchTrelloDetails(item, list))
    return items

def get_list_id(name):
    api_key = os.getenv("TRELLO_API_KEY")
    board_id = os.getenv("TRELLO_BOARD_ID")
    token = os.getenv("TRELLO_TOKEN")

    url = f"https://api.trello.com/1/boards/{board_id}/lists?key={api_key}&token={token}"
    response = requests.request("GET", url, headers=headers).json()
    return next(list["id"] for list in response if list["name"] == name)

def add_item(title, description):
    api_key = os.getenv("TRELLO_API_KEY")
    token = os.getenv("TRELLO_TOKEN")

    list_id = get_list_id("To Do")
    url = f"https://api.trello.com/1/cards?key={api_key}&token={token}&desc={description}&name={title}&idList={list_id}"
    print(requests.request("POST", url, headers=headers))

def progress_item(id: str):
    api_key = os.getenv("TRELLO_API_KEY")
    token = os.getenv("TRELLO_TOKEN")

    list_id_progress = get_list_id("In Progress")
    url = f"https://api.trello.com/1/cards/{id}?key={api_key}&token={token}&idList={list_id_progress}"
    requests.request("PUT", url, headers=headers)

def complete_item(id: str):
    api_key = os.getenv("TRELLO_API_KEY")
    token = os.getenv("TRELLO_TOKEN")

    list_id_complete = get_list_id("Done")
    url = f"https://api.trello.com/1/cards/{id}?key={api_key}&token={token}&idList={list_id_complete}"
    requests.request("PUT", url, headers=headers)

def remove_item(id: str):
    api_key = os.getenv("TRELLO_API_KEY")
    token = os.getenv("TRELLO_TOKEN")
    
    url = f"https://api.trello.com/1/cards/{id}?key={api_key}&token={token}"
    requests.request("DELETE", url, headers=headers)