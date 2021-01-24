import json
import requests

# An api key is emailed to you when you sign up to a plan
api_key = 'ea000872e35c4034fee1ae19399b1cc0'

#First get a list of in-season sports
sports_response = requests.get('https://api.the-odds-api.com/v3/sports', params={
    'api_key': api_key
})

sports_json = json.loads(sports_response.text)
league_keys = []


if not sports_json['success']:
    print(
        'There was a problem with the sports request:',
        sports_json['msg']
    )

else:
    print()
    print(
        'Successfully got {} sports'.format(len(sports_json['data'])),
        'Here\'s the sports:'
    )

for sport in sports_json['data']:
    if(sport['group'][0:6] == 'Soccer'):
        print(sport['key'])
        league_keys.append(sport['key'])





# To get odds for a sepcific sport, use the sport key from the last request
#   or set sport to "upcoming" to see live and upcoming across all sports
sport_key = 'upcoming'

odds_response = requests.get('https://api.the-odds-api.com/v3/odds', params={
    'api_key': api_key,
    'sport': sport_key,
    'region': 'uk', # uk | us | eu | au
    'mkt': 'spreads' # h2h | spreads | totals
})

odds_json = json.loads(odds_response.text)
if not odds_json['success']:
    print(
        'There was a problem with the odds request:',
        odds_json['msg']
    )

else:
    # odds_json['data'] contains a list of live and 
    #   upcoming events and odds for different bookmakers.
    # Events are ordered by start time (live events are first)
    print()
    print(
        'Successfully got {} events'.format(len(odds_json['data'])),
        'Here\'s the first event:'
    )

    for x in range(10):
        print()    

    for odd in odds_json['data']:
        if (odd['sport_key'] in league_keys):
            for site in odd['sites']:
                print(odd['sport_key'], odd['teams'], site['odds'])


    # Check your usage
    print()
    print('Remaining requests', odds_response.headers['x-requests-remaining'])
    print('Used requests', odds_response.headers['x-requests-used'])
