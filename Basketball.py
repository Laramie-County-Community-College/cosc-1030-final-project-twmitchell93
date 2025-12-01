import random


THREE_PT_PCT = 0.35         # your 3-point percentage
TWO_PT_PCT = 0.55           # your 2-point percentage
OPP_FT_PCT = 0.65           # opponent free-throw percentage
OFF_REB_PCT = 0.25          # chance you get an offensive rebound
OT_WIN_PROB = 0.50          # probability you win in overtime
TIME_REMAINING = 30         # starting time (seconds)
TRIALS = 10000              # number of Monte Carlo simulations

# -----------------------------
# SIMULATION FUNCTIONS
# -----------------------------

def simulate_take_three():
    """Simulates scenario where team shoots a 3 while down 3."""

    # Shoot the 3-pointer
    if random.random() < THREE_PT_PCT:
        # You made the 3 → game tied → overtime
        return random.random() < OT_WIN_PROB
    else:
        # Missed → try for offensive rebound
        if random.random() < OFF_REB_PCT:
            # Take another 3
            if random.random() < THREE_PT_PCT:
                return random.random() < OT_WIN_PROB
        # Miss again → lose
        return False


def simulate_take_two_and_foul():
    """
    Simulates scenario where the team takes an easy 2,
    then fouls and hopes opponent misses at least one FT.
    """

    # Make or miss the 2-pointer?
    made_two = random.random() < TWO_PT_PCT

    if not made_two:
        return False  # missed the 2 → lose immediately

    # Now down 1 and foul opponent
    ft1 = random.random() < OPP_FT_PCT
    ft2 = random.random() < OPP_FT_PCT

    opp_points = ft1 + ft2  # 0, 1, or 2 points

    # After free throws: you are down 1, 2, or 3
    # Must get the ball back with about ~7 seconds left

    # You get final possession:
    if opp_points == 0:
        # Down 1 → can win with a 2
        return random.random() < TWO_PT_PCT
    elif opp_points == 1:
        # Down 2 → must tie with a 2 → overtime
        if random.random() < TWO_PT_PCT:
            return random.random() < OT_WIN_PROB
        return False
    else:
        # Down 3 → must hit a 3 → overtime
        if random.random() < THREE_PT_PCT:
            return random.random() < OT_WIN_PROB
        return False


# -----------------------------
# RUN MONTE CARLO SIMULATION
# -----------------------------

wins_three = 0
wins_two_foul = 0

for _ in range(TRIALS):
    if simulate_take_three():
        wins_three += 1
    if simulate_take_two_and_foul():
        wins_two_foul += 1

# -----------------------------
# OUTPUT RESULTS
# -----------------------------

print("----- RESULTS -----")
print(f"Trials run: {TRIALS}")
print()

print("STRATEGY 1: Shoot a 3 while down 3")
print(f"Win rate: {wins_three / TRIALS * 100:.2f}%")

print("\nSTRATEGY 2: Take a 2, then foul")
print(f"Win rate: {wins_two_foul / TRIALS * 100:.2f}%")
