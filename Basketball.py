import random

# My basketball simulation project
# Compare shooting a 3-pointer vs taking a 2 and fouling in the last 30 seconds

# PARAMETERS
three_point_chance = 0.35       # chance to make a 3-pointer
two_point_chance = 0.55         # chance to make a 2-pointer
opp_free_throw = 0.65           # opponent free throw chance
offensive_rebound = 0.25        # chance to grab an offensive rebound
overtime_win = 0.5              # chance to win in overtime
num_simulations = 10000         # number of simulation trials

# Function: try shooting a 3-pointer
def try_three():
    points = 0
    if random.random() < three_point_chance:
        points += 3
        win = random.random() < overtime_win
        return win, points
    else:
        if random.random() < offensive_rebound:
            if random.random() < three_point_chance:
                points += 3
                win = random.random() < overtime_win
                return win, points
        return False, points

# Function: take a 2-pointer and then foul
def try_two_and_foul():
    points = 0
    made_two = random.random() < two_point_chance
    if made_two:
        points += 2
    else:
        return False, points

    # Foul opponent
    ft1 = random.random() < opp_free_throw
    ft2 = random.random() < opp_free_throw
    opp_points = ft1 + ft2

    if opp_points == 0:
        if random.random() < two_point_chance:
            points += 2
            return True, points
        return False, points
    elif opp_points == 1:
        if random.random() < two_point_chance:
            points += 2
            win = random.random() < overtime_win
            return win, points
        return False, points
    else:
        if random.random() < three_point_chance:
            points += 3
            win = random.random() < overtime_win
            return win, points
        return False, points

# RUN SIMULATION
wins_three = 0
wins_two = 0
total_points_three = 0
total_points_two = 0

for _ in range(num_simulations):
    win, pts = try_three()
    if win:
        wins_three += 1
    total_points_three += pts

    win, pts = try_two_and_foul()
    if win:
        wins_two += 1
    total_points_two += pts

# PRINT RESULTS
print("----- RESULTS -----")
print(f"Simulations run: {num_simulations}\n")
print("STRATEGY 1: Shoot a 3")
print(f"Win rate: {wins_three / num_simulations * 100:.2f}%")
print(f"Average points scored: {total_points_three / num_simulations:.2f}\n")
print("STRATEGY 2: Take a 2 then foul")
print(f"Win rate: {wins_two / num_simulations * 100:.2f}%")
print(f"Average points scored: {total_points_two / num_simulations:.2f}")