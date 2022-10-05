# Import user-specified data from Statsbomb using custom football data module 

#%% Imports

import os
import sys
from statsbombpy import sb

# %% Add custom tools to path

root_folder = os.path.abspath(os.path.dirname((os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(root_folder)

import analysis_tools.get_football_data as gfd

# %% Fetch username and password fron environment variables

USERNAME = os.environ.get("STATSBOMB_USERNAME")
PASSWORD = os.environ.get("STATSBOMB_PASSWORD")

# %% Get available competitions and matches

#available_comps = sb.competitions(creds = {"user": USERNAME, "passwd": PASSWORD})
#available_matches = sb.matches(competition_id=3, season_id=235, creds = {"user": USERNAME, "passwd": PASSWORD})

# %% User inputs

# Input competition name (Statsbomb convention)
competition = 'Championship'

# Input competition year(s)
year = '2022/2023'

# %% Obtain and save data

if '/' in year:
    year_str = year[0:4]
else:
    year_str = year

# Obtain and save data using custom function
events, lineups, matches = gfd.get_statsbomb_data(competition, year, username=USERNAME, password=PASSWORD, save_to_file=True, folderpath=f"../../data_directory/statsbomb_data/{int(year_str)}_{str(int(year_str.replace('20',''))+1)}/{competition}")