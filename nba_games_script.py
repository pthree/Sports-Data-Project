import json
import urllib2
import csv
import sys
import time

game_ids = []	#Create empty list to store Game IDs
api_token = '' #token goes here

writer = csv.writer(open("/yourdirectory/nba_games.csv", 'w')) #add path to your csv file

data_games = json.load(urllib2.urlopen('http://api.sportsdatallc.org/nba-t3/games/2013/REG/schedule.json?api_key=' + api_token))
data_playoffs = json.load(urllib2.urlopen('http://api.sportsdatallc.org/nba-t3/series/2013/PST/schedule.json?api_key=' + api_token))

games = data_games['games']
for game in games:
	game_id = game['id']
	series_id = ''
	game_status = game['status']
	game_title = ''
	home_team_id = game['home']['id']
	away_team_id = game['away']['id']
	home_team_alias = game['home']['alias']
	away_team_alias = game['away']['alias']
	scheduled = game['scheduled']

	writer.writerow([game_id, series_id, game_status, game_title, home_team_id, away_team_id, home_team_alias, away_team_alias, scheduled])	

series = data_playoffs['series']
for playoff_series in series:
	for game in playoff_series['games']:
		game_id = game['id']
		series_id = playoff_series['id']
		game_status = game['status']
		game_title = playoff_series['title']
		home_team_id = game['home']['id']
		away_team_id = game['away']['id']
		home_team_alias = game['home']['alias']
		away_team_alias = game['away']['alias']
		scheduled = game['scheduled']

		writer.writerow([game_id, series_id, game_status, game_title, home_team_id, away_team_id, home_team_alias, away_team_alias, scheduled])	