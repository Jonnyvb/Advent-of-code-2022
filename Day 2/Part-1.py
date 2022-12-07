
# A, X : Rock
# B, Y : Paper
# C, Z : Scissors

# Rock = 1pt
# Paper = 2pt
# Scissors = 3pt

# Lose = 0pt
# Draw = 3pt
# Win = 6pt

if __name__ == "__main__":
    with open("./Day 2/Input.txt") as f:
        score = 0
        for line in f:
            line = line.replace("\n", "")
            opponentThrow, myThrow = line.split(" ")
            gameState = opponentThrow + myThrow
            
            if gameState == "AX":
                score += 4
            elif gameState == "AY":
                score += 8
            elif gameState == "AZ":
                score += 3
            elif gameState == "BX":
                score += 1
            elif gameState == "BY":
                score += 5
            elif gameState == "BZ":
                score += 9
            elif gameState == "CX":
                score += 7
            elif gameState == "CY":
                score += 2
            elif gameState == "CZ":
                score += 6

    print(score)