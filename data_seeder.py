#Seeding last 5 season of NBA stats to a local CSV to perform data analysis

from nba_api.stats.endpoints.leaguegamefinder import LeagueGameFinder
from nba_api.stats.static import teams
import pandas as pd
import time

def seed_data(seasons, type_abbrev: str, filename):
    all_data = []
    
    nba_teams = teams.get_teams()

    team_ids = [team['id'] for team in nba_teams]

    print(f"Seeding data for {type_abbrev}...")

    for season in seasons:
        print(f"Fetching season {season}")
        
        if type_abbrev == 'P':
            for team_id in team_ids:
                try:
                    game_finder = LeagueGameFinder(season_nullable=season, 
                                                   player_or_team_abbreviation=type_abbrev,
                                                   team_id_nullable= team_id)
                    team_season_df = game_finder.get_data_frames()[0]
                    all_data.append(team_season_df)
                    print(f"Got {len(team_season_df)} rows for Team {team_id}")
                    time.sleep(0.5)
                except Exception as e:
                    print(f"Error fetching team {team_id}: {e}")
        
        else:
            game_finder = LeagueGameFinder(season_nullable=season, player_or_team_abbreviation=type_abbrev)
            season_df = game_finder.get_data_frames()[0]
            all_data.append(season_df)
            print(f"Got {len(season_df)} rows for entire league")
            time.sleep(1)
    print("Successfully fetched all seasons")
    final_df = pd.concat(all_data)
    final_df.to_csv(filename,index=False)
    print(f"Saved {filename}")
    
seasons_fetch = ['2024-25','2023-24','2022-23','2021-22','2020-21', '2019-20','2018-19','2017-18']

#T is for seeding team stats, P is for seeding player stats
seed_data(seasons_fetch, 'T', 'nba_team_data.csv')
seed_data(seasons_fetch, 'P', 'nba_player_data.csv')
