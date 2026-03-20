def expected_result(player_utr, opponent_utr):
    """Probability of player winning against opponent"""
    return 1 / (1 + 10 ** ((opponent_utr - player_utr) / 2))

def update_utr(player_utr, opponent_utr, games_won, games_lost):
    """Update UTR after a match"""
    expected = expected_result(player_utr, opponent_utr)
    actual = 1 if games_won > games_lost else 0

    # margin of victory
    margin = (games_won - games_lost) / (games_won + games_lost) if (games_won + games_lost) > 0 else 0
    margin_factor = 1 + margin

    K = 0.3  # sensitivity factor
    rating_change = K * (actual - expected) * margin_factor

    new_utr = player_utr + rating_change
    return round(new_utr, 2)