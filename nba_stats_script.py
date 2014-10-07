import json
import urllib2
import csv
import sys
import time

game_ids = []	#Create empty list to store Game IDs
api_token = '' #Token goes here

with open('nba_gameid_mod.csv', 'rU') as csvfile:
    games = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in games:
        game_ids.extend(row)

writer = csv.writer(open("/yourpath/nba.csv", 'w')) #update the path to your own file

for game_id in game_ids:	#loop through list of Game IDs
	pbp_url = 'http://api.sportsdatallc.org/nba-t3/games/' + game_id + '/pbp.json?api_key=' + api_token
	data = json.load(urllib2.urlopen(pbp_url))	#store API call in data variable
	quarters = data['periods']	

	for quarter in quarters:	
		events = quarter['events']
		for event in events:
			id = event['id']
			type = event['event_type'] 
			clock = event['clock']
			description = event['description']
			possession_name = event.get('possession', {}).get('name')
			team_basket = event.get('attribution', {}).get('team_basket')
			locationx = event.get('location', {}).get('coord_x')
			locationy = event.get('location', {}).get('coord_y')
			player = event.get('statistics',{})
			if player:	#only store events with player stats 
				for play in player:
					player2 = play.get('player', {}).get('full_name')
					team = play.get('team', {}).get('name')
					type2 = play.get('type')
					made = play.get('made','')
					line = [id, data['id'], type, clock, description, team_basket, locationx, locationy, possession_name, player2, type2, made, team, quarter['id']]
					writer.writerow(line)	
	
	time.sleep(1) #ensures API calls are made at least 1 second apart due to API limit
					
