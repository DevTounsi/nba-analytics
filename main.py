from nba_api.stats.endpoints import playercareerstats as pcs
import json
from nba_api.stats.static import players
import pandas as pd
# Chercher Kevin Durant
'''kd = players.find_players_by_full_name("Kevin Durant")
print(kd)
career = pcs.PlayerCareerStats(player_id=kd[0]['id'])
career_json = career.get_json()
print(career)

# Écriture dans le fichier test.json
with open('test.json', 'w') as f:
    json.dump(json.loads(career_json), f, indent=4)'''
sc_player = players.find_players_by_first_name("Durant")


print(sc_player)
