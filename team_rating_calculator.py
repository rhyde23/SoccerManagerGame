#Calculate Team Rating

from starting_team_formations import get_positions_from_formation
from outside_positions_converter import convert_outside_position_to_center
from energy_rating_modifier import adjust_for_energy

def get_real_rating(player, lineup, formation, players) :
    current_position = get_positions_from_formation(formation)[lineup.index(player)]
    current_position = convert_outside_position_to_center(current_position)
    return players[player]['Positions'][current_position]

def calculate_rating(players, lineup, formation, significance_percentage, energies) :
    ratings = [adjust_for_energy(int(get_real_rating(player, lineup, formation, players)), significance_percentage, energies[player]) for player in lineup]
    #print(lineup)
    #print(ratings)
    return int(sum(ratings)/11)
