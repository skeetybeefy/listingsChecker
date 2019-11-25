import requests
from datetime import datetime
import time
import json


# Getting info about cases

query = 'case'
start = 0  # Get information starting from this item
count = 100  # Number of results (100 is max)
URL = f'https://steamcommunity.com/market/search/' \
      f'render/?norender=1&query={query}&start={start}&count={count}&search_descriptions=0&sort_column=default&' \
      f'sort_dir=desc&appid=730&category_730_ItemSet%5B%5D=any&' \
      f'category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&' \
      f'category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase'

# URL above is a request to Steam when switching pages on Community Market

r = requests.get(URL).text


date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Get current time of a request


def createItems():
    if r != 'null':
        response = json.loads(r)
        items = []
        for item in response["results"]:  # Creating a dict with all information of each item from response
            itemData = {
                'date': date,
                'name': item["hash_name"],
                'price': item["sell_price_text"],
                'listings': item["sell_listings"]
            }
            print(itemData)
            items.append(itemData)

    else:
        print(f'You made too many requests to Steam or there is a network problem')
        time.sleep(2)

    return items  # Returning list with all items as objects


