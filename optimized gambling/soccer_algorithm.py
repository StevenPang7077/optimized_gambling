import gambling_api_connection as gac
import math

recomendations = []



def main(games):
	all_games = games #take their imput
	rec_list = []
	for game in all_games:
		rec = calculate(game)
		if(rec):
			rec_list.append(rec)
			print(rec)
	return(rec_list)

def calculate(game):
	if (game['sites']):
		max_spread = -9999999999
		min_spread = 9999999999
		max_spread_site = ""
		min_spread_site = ""
	else:
		max_spread = 0
		min_spread = 0

	for site in game['sites']:
		# print(site)
		if (float(site['odds']['spreads']['points'][0]) < min_spread):
			min_spread = float(site['odds']['spreads']['points'][0])
			min_spread_site = site['site_key']
		if (float(site['odds']['spreads']['points'][0]) > max_spread):
			max_spread = float(site['odds']['spreads']['points'][0])
			max_spread_site = site['site_key']


	# print("max: " + str(max_spread))
	# print("min: " + str(min_spread))
	# print("diff: " + str(max_spread-min_spread))
	#print(math.floor(max_spread))
	if (max_spread - min_spread > 1 or (max_spread-min_spread == 1 and math.floor(max_spread) != max_spread)):
		rec = {
		'team': game['game_name']['team'][0], 
		'website_in_favor': min_spread_site, 
		'website_against': max_spread_site,
		'game': game['game_name'],
		'start': game['game_name']['commence_time'],
		'max': max_spread,
		'min': min_spread,
		}
		return rec








