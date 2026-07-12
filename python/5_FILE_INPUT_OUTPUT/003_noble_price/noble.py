# you'll create a program to query a collection of Nobel prize winners by year or by category or switch.

import json
import helper 

def load_nobel_prizes(filename='price.json'):
    with open(filename) as f:
        return json.load(f)


def main(year, category):
    data = load_nobel_prizes()
    prizes = data['prizes']

    for prize in prizes:
        if 'laureates' not in prize:
            continue
        if category and prize['category'].lower() != category.lower():
            continue
        if year and prize['year'] != year:
            continue

        print(f"{prize['year']} Nobel Prize in {prize['category'].title()}")
        for laureate in prize['laureates']:
            firstname = laureate['firstname']
            surname = laureate.get('surname', '')
            print(f"{firstname} {surname}: {laureate['motivation']}")

if __name__ == '__main__':

    year = input('Enter year, or leave blank for all years: ').strip()
    category = input('Enter category, or leave blank for all categories: ').strip()
    main(year, category)