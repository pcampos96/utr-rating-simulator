'''
This program generates sample match data 
'''
import csv
import random

def generate_match_data():
    players = ["Alice", "Bob", "Charlie", "Dana"]
    num_matches = 30

    with open("sample_matches.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["player","opponent","games_won","games_lost","player_utr","opponent_utr"])
        
        for _ in range(num_matches):
            player = random.choice(players)
            opponent = random.choice([p for p in players if p != player])
            games_won = random.randint(0, 6)
            games_lost = random.randint(0, 6)
            player_utr = round(random.uniform(4.0, 10.0), 2)
            opponent_utr = round(random.uniform(4.0, 10.0), 2)
            writer.writerow([player, opponent, games_won, games_lost, player_utr, opponent_utr])

    print("Sample CSV 'sample_matches.csv' created!")