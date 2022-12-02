def read_puzzle(file):
    return [[info for info in round.split(" ")] for round in open(file).read().strip().split("\n")]

#A for Rock, B for Paper, and C for Scissors. 
Opponent = {"A" : "ROCK", "B" : "PAPER", "C" : "SCISSORS"}

# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.
Wins = {("ROCK", "SCISSORS"), ("SCISSORS", "PAPER"), ("PAPER", "ROCK")}

#shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
Shape = {"ROCK" : 1, "PAPER" : 2, "SCISSORS" : 3}

def Score(opponent, me):
    # score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
    score = 0
    if opponent == me:
        score = 3
    else:
        score =  6 if (me, opponent) in Wins else 0
    score += Shape[me]
    return score

def play_1(opponent, me):
    #X for Rock, Y for Paper, and Z for Scissors. 
    Me = {"X" : "ROCK", "Y" : "PAPER", "Z" : "SCISSORS"}
    opponent = Opponent[opponent]
    me = Me[me]
    return Score(opponent, me)

def play_2(opponent, me):
    Me_Lose = {"ROCK": "SCISSORS", "SCISSORS": "PAPER", "PAPER": "ROCK"}
    Me_Wins  = {"SCISSORS": "ROCK", "PAPER": "SCISSORS", "ROCK": "PAPER"}
    #X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
    opponent = Opponent[opponent]
    if me == "X":
        me = Me_Lose[opponent]
    elif me == "Z":
        me = Me_Wins[opponent]
    else:
        me = opponent
    return Score(opponent, me)
    
def solve(puzzle):
    score_1 = 0
    score_2 = 0
    for round in puzzle:
        s_1 = play_1(*round)
        s_2 = play_2(*round)
        score_1 += s_1
        score_2 += s_2
    return score_1, score_2
        
puzzle = read_puzzle('d02.txt')

results = solve(puzzle)

print(f"Task1: {results[0]}")
print(f"Task1: {results[1]}")