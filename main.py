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
player_id = 201142  # Kevin Durant
career = pcs.PlayerCareerStats(player_id=player_id)

# Correct : get_data_frames()
df = career.get_data_frames()[1]
print(df.columns)
print(df.head(10))