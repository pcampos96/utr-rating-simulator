import csv
import random
from match_data_generator import generate_match_data
from Elo_UTR_functions import expected_result, update_utr

# Create sample data csv file 
generate_match_data()

# Read CSV and Simulate UTR Updates

utr_table = {}  # store current UTR for each player

with open("sample_matches.csv", "r") as file:
    reader = csv.DictReader(file)
    
    print("\nSimulating Matches...\n")
    for row in reader:
        player = row["player"]
        opponent = row["opponent"]
        games_won = int(row["games_won"])
        games_lost = int(row["games_lost"])
        player_utr = float(row["player_utr"])
        opponent_utr = float(row["opponent_utr"])
        
        # Use latest UTR if player already played previous matches
        player_utr = utr_table.get(player, player_utr)
        
        # Update UTR
        new_utr = update_utr(player_utr, opponent_utr, games_won, games_lost)
        utr_table[player] = new_utr
        
        print(f"{player} vs {opponent} | Score: {games_won}-{games_lost} | Old UTR: {player_utr} -> New UTR: {new_utr}")

# Output Final UTR Rankings
print("\nFinal UTRs after all matches:")
for player, utr in utr_table.items():
    print(f"{player}: {utr}")