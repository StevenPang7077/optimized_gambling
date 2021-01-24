import json
import requests

# An api key is emailed to you when you sign up to a plan
api_key = 'ea000872e35c4034fee1ae19399b1cc0'

#First get a list of in-season sports
def get_response():
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
    locations = ['uk', 'us', 'eu', 'au']
    odds_json = {'data':[]}
    x = 0
    for key in league_keys:
        for location in locations:
            sport_key = key
            

            odds_response = requests.get('https://api.the-odds-api.com/v3/odds', params={
                'api_key': api_key,
                'sport': sport_key,
                'region': location, # uk | us | eu | au
                'mkt': 'spreads' # h2h | spreads | totals
            })

            odds_json['data'] = odds_json['data']+(json.loads(odds_response.text))['data']
            # if not odds_json['success']:
            #     print(
            #         'There was a problem with the odds request:',
            #         odds_json['msg']
            #     )

            # else:
            #     # odds_json['data'] contains a list of live and
            #     #   upcoming events and odds for different bookmakers.
            #     # Events are ordered by sta

            #     pass

                # for odd in odds_json['data']:
                #     if (odd['sport_key'] in league_keys):
                #         for site in odd['sites']:
                #             print(odd['sport_key'], odd['teams'], site['odds'])


            # Check your usage
            print("requests made: " + str(x))
            x = x + 1
            # print('Remaining requests', odds_response.headers['x-requests-remaining'])
            # print('Used requests', odds_response.headers['x-requests-used'])
    #print(odds_json['data'])

    game_array = []             
    for odd in odds_json['data']:
       
        game_array.append({
                'game_name': {'commence_time': odd['commence_time'],
                           'team': odd['teams'],
                           'sport_key': odd['sport_key'],
                           },
                'sites': odd['sites']
        })

    return(game_array)
   
        #game = {}
       # if (game in game_array):
         
       
    #games = {name: 'commence_time', }
   
    #if(odd[''])