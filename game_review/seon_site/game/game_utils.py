import urllib.request
import requests
import json

def get_game_id(title):
    base_url = "https://api.steampowered.com/ISteamApps/GetAppList/v2"

    # URL에서 JSON 데이터를 직접 읽어옴
    with urllib.request.urlopen(base_url) as url:
        data = json.loads(url.read().decode('utf-8'))

    game_list = data["applist"]["apps"]

    for game in game_list:
        if game["name"].lower() == title.lower():
            return game["appid"]

# print(get_game_id("ELDEN RING"))

def get_game_trailer(app_id):
    base_url = f"http://store.steampowered.com/api/appdetails?appids={app_id}&l=korean"

    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        movies = data[str(app_id)]["data"]["movies"]
    
        if movies:
            webm_info = movies[0]["webm"]
            if "max" in webm_info:
                trailer = webm_info["max"]
                return trailer

def get_game_detail(app_id):
    base_url = f"http://store.steampowered.com/api/appdetails?appids={app_id}&l=korean"

    response = requests.get(base_url)
    data = response.json()

    details = data[str(app_id)]["data"]["short_description"]
    return details

# print(get_game_detail(get_game_id("ELDEN RING")))

def get_game_image(app_id):
    base_url = f"http://store.steampowered.com/api/appdetails?appids={app_id}&l=korean"

    response = requests.get(base_url)
    data = response.json()

    game_image = data[str(app_id)]["data"]["header_image"]
    return game_image