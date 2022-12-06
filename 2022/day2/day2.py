# Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle input) that they say will be sure to help you win. "The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.

# The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors. Winning every time would be suspicious, so the responses must have been carefully chosen.

# The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

# x = loose
# y = draw
# z = win

scores = {
    "A X": 3, # 0 + 3
    "A Y": 4, # 3 + 1
    "A Z": 8, # 6 + 2

    "B X": 1, # 0 + 1
    "B Y": 5, # 3 + 2
    "B Z": 9, # 6 + 3

    "C X": 2, # 0 + 2
    "C Y": 6, # 3 + 3
    "C Z": 7, # 6 + 1
}

score = 0
f = open("input.txt", "r")
for x in f:
    score = score + scores[x.strip()]

print("Answer 2: " + str(score))
