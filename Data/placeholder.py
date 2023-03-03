import argparse
import requests
from bs4 import BeautifulSoup
import json


# Makes sure hotness only returns a number
def parse_itemssold(text):
    numbers = ''
    for char in text:
        if char in '1234567890':
            numbers += char
    if 'sold' in text:
        return int(numbers)
    else:
        return 0

def parse_itemsshipping(text):
    numbers = ''
    for char in text:
        if char in '1234567890.':
            numbers += char
    if 'Free' in text:
        return '0'
    else:
        return numbers

if __name__ == '__main__':
    
    # Get command line arguments
    parser = argparse.ArgumentParser(description='Download information from ebay and convert to JSON.')
    parser.add_argument('search_term')
    parser.add_argument('--num_pages',default=10)
    args = parser.parse_args()
    print('args.search_terms=', args.search_term)

    # All items found
    items = []

    for page_number in range(1, int(args.num_pages) + 1):
        #Build the URL
        url = 'https://www.baseball-reference.com/teams/' 
    url += args.team.replace(' ','+')
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

        tags_items = soup.select('.s-item')
        
        for tag_item in tags_items:
            
            # Extract the name
            tags_name = tag_item.select('.s-item__title')
            name = None
            for tag in tags_name:
                name = tag.text

            # Extract the price
            tags_name = tag_item.select('.s-item__price')
            price = None
            for tag in tags_name:
                price = tag.text

            # Extract the item condition
            tags_name = tag_item.select('.s-item__subtitle')
            item_condition = None
            for tag in tags_name:
                item_condition = tag.text

            # Extract the shipping price
            tags_name = tag_item.select('.s-item__shipping')
            shipping_price = 0
            for tag in tags_name:
                shipping_price = parse_itemsshipping(tag.text)

            # Extract the free returns
            freereturns = False
            tags_freereturns = tag_item.select('.s-item__free-returns')
            for tag in tags_freereturns:
                freereturns = True

            # Extract the the number of items sold
            tags_name = tag_item.select('.s-item__hotness')
            items_sold = 0
            for tag in tags_name:
                items_sold = parse_itemssold(tag.text)

            # Creates the dictionary for each item
            item = {
                'name': name,
                'price': price,
                'status': item_condition,
                'shipping_price': shipping_price,
                'free_returns': freereturns,
                'items_sold': items_sold,
            }
            items.append(item)

        print('len(tag_items)=',len(tags_items))
        print('len(items)', len(items))

    # Write the json into a file
    filename = args.search_term + '.json'
    with open(filename, 'w', encoding='ascii') as f:
        f.write(json.dumps(items))