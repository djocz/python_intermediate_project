# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"

# Enter Code Here
def get_unique_teams_set():
    ipl_matches_array = read_ipl_data_csv(path,'S50')
    matches = ipl_matches_array[:,(3,4)]
    unique_teams = np.unique(matches)
    return set(unique_teams)
