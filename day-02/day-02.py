def read_file(param):
    with open(param, 'r') as f:
        return f.read()


basic_score_calculations = {"A X": 1 + 3, "B X": 1 + 0, "C X": 1 + 6, "A Y": 2 + 6, "B Y": 2 + 3, "C Y": 2 + 0,
                            "A Z": 3 + 0, "B Z": 3 + 6, "C Z": 3 + 3}

your_action_calculations = {"A X": 0 + 3,  # opp chooses rock, we need to lose, we chose scissors
                            "B X": 0 + 1,  # opp chooses paper, we need to lose, we chose rock
                            "C X": 0 + 2,  # opp chooses scissor, we need to lose, we chose paper
                            "A Y": 3 + 1,  # opp chooses rock, we need to draw, we chose rock
                            "B Y": 3 + 2,  # opp chooses paper, we need to draw, we chose paper
                            "C Y": 3 + 3,  # opp chooses scissor, we need to draw, we chose scissor
                            "A Z": 6 + 2,  # opp chooses rock, we need to win, we chose paper
                            "B Z": 6 + 3,  # opp chooses paper, we need to win, we chose scissor
                            "C Z": 6 + 1,  # opp chooses scissor, we need to win, we chose rock
                            }

if __name__ == "__main__":
    lines = read_file("day-02/day-02-input.txt")

    score_basic = 0
    score_advanced = 0

    for line in lines.splitlines():
        score_basic = score_basic + basic_score_calculations[line]
        score_advanced = score_advanced + your_action_calculations[line]

    print("Score (puzzle 1): " + str(score_basic))
    print("Score (puzzle 2): " + str(score_advanced))
