
from pprint import pprint
import requests

def the_cleverest_superhero():
    url = 'https://superheroapi.com/api/2619421814940190/search'
    superhero_crew = ['Hulk', 'Captain America', 'Thanos']

    the_cleverest_hero = {'name': '', 'intelligence': 0}
    for hero in superhero_crew:
        response = requests.get(url=url + '/' + hero, timeout=5)
        if response.status_code == 200:
            response_content = response.json()
            intelligence_rate = response_content['results'][0]['powerstats']['intelligence']
            if int(intelligence_rate) > int(the_cleverest_hero['intelligence']):
                the_cleverest_hero['name'] = hero
                the_cleverest_hero['intelligence'] = intelligence_rate
    return the_cleverest_hero

if __name__ == '__main__':
    result = the_cleverest_superhero()
    print(f'Самый умный супергерой: {result["name"]}. Уровень: {result["intelligence"]}')