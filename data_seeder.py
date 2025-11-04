#Seeding last 5 season of NBA stats to a local CSV to perform data analysis

from nba_api.stats.endpoints.leaguegamefinder import LeagueGameFinder
import pandas as pd
import time

seasons_fetch = ['2024-25','2023-24', '2022-23', '2021-22','2020-21']
all_seasons = []


for season in seasons_fetch:
    print(f"Fetching season {season}")
    game_finder = LeagueGameFinder(season_nullable=season)
    season_df = game_finder.get_data_frames()[0]
    all_seasons.append(season_df)
    print(f"Successfully appended {len(season_df)} game records for {season}")
    time.sleep(1)
print("Successfully fetched all seasons")
final_df = pd.concat(all_seasons)

print(f"Total games in final DataFrame: {len(final_df)}")
print(f"Saving to csv")
final_df.to_csv('nba_data.csv',index=False)
print("All done")