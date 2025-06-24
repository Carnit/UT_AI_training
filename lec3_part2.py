import random
from typing import Dict, List


def simulate_dice_game(player_names: List[str], total_rounds: int = 10) -> None:
    scores: Dict[str, int] = {player: 0 for player in player_names}
    last_rolls: Dict[str, int] = {player: 0 for player in player_names}

    round_num: int = 1
    while round_num <= total_rounds:
        print(f"\nRound {round_num}")
        for player in player_names:
            roll: int = random.randint(1, 6)
            print(f"{player} rolls a {roll}", end="")

            # Apply main rules
            if roll == 6:
                scores[player] += 10
                print(" → +10 points", end="")
                if last_rolls[player] == 6:
                    scores[player] += 5
                    print("BONUS! (Two 6s) +5", end="")
            elif roll == 1:
                scores[player] -= 5
                print(" → -5 points", end="")
            else:
                scores[player] += roll
                print(f" → +{roll} points", end="")

            last_rolls[player] = roll
            print(f" | Total: {scores[player]}")

        round_num += 1

    print("\nFinal Scores:")
    for player, score in scores.items():
        print(f"{player}: {score}")

    # Use lambda to find winner(s)
    max_score = max(scores.values())
    winners = list(filter(lambda p: scores[p] == max_score, scores))

    print("\nWinner:")
    for winner in winners:
        print(f"- {winner} with {max_score} points")


# --- Entry Point ---
if __name__ == "__main__":
    print("Welcome to the Dice Game")
    num_players: int = int(input("Enter number of players: "))
    player_names: List[str] = []

    for i in range(num_players):
        name = input(f"Enter name for Player {i + 1}: ").strip()
        player_names.append(name)

    simulate_dice_game(player_names)
