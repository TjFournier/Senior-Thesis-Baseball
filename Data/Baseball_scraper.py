import argparse
import requests
from bs4 import BeautifulSoup
import json


if __name__ == '__main__':


    # All items found
    items = []

    
    #Build the URL
    url = 'https://www.baseball-reference.com/teams/ARI/2019-schedule-scores.shtml' 
    

    # download the HTML
    r = requests.get(url)
    status = r.status_code
    print('status=', status)
    html = r.text

    # process the html
        
    soup = BeautifulSoup(html, 'html.parser')
    
    schedule_table = soup.find('table',class_= 'sortable stats_table')
    
    for game in schedule_table.find_all('tbody'):
        rows = game.find_all('tr')

        for row in rows:
            game_number = row.find('th', class_='right')
            print(game_number)