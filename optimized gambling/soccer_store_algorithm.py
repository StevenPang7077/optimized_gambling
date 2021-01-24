import soccer_algorithm as soc_al, gambling_api_connection as gac, csv, between

recs = soc_al.main(gac.get_response())

with open('bets.csv', 'w', newline='') as csvfile:
	fieldnames = ['start', 'num_opps', 'teams', 'website_in_favor', 'website_against', 'game',]
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	for rec in recs:
		writer.writerow({
			'start': rec['start'], 
			'num_opps': between.whole_btwn(rec['max'], rec['min']),
			'teams':rec['team'], 
			'website_in_favor': rec['website_in_favor'], 
			'website_against': rec['website_against'],
			'game':rec['game'],
			})