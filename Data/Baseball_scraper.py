import argparse
import requests
from bs4 import BeautifulSoup
import json


if __name__ == '__main__':
    
    # Get command line arguments
    parser = argparse.ArgumentParser(description='Download information from ebay and convert to JSON.')
    parser.add_argument('team')
    parser.add_argument('--year',)
    args = parser.parse_args()
    print('args.search_terms=', args.search_term)

    # All items found
    items = []

    
    #Build the URL
    url = 'https://www.baseball-reference.com/teams/' 
    url += args.search_term.replace(' ','+')
    url += '/'
    url += str(args.year)
    url += '-schedule-scores.shtml'
    print('url=',url)

    # download the HTML
    r = requests.get(url)
    status = r.status_code
    print('status=', status)
    html = r.text

    # process the html
    
    soup = BeautifulSoup(html, 'html.parser')

    tags_items = soup.select('data-row')
    
    for tag_item in tags_items:
        
        # Extract the team name
        tags_name = tag_item.select('team_ID')
        name = None
        for tag in tags_name:
            name = tag.text

        # Creates the dictionary for each item
        item = {
            'name': name,
            
        }
        items.append(item)

        print('len(tag_items)=',len(tags_items))
        print('len(items)', len(items))

    # Write the json into a file
    filename = args.search_term + '.json'
    with open(filename, 'w', encoding='ascii') as f:
        f.write(json.dumps(items))