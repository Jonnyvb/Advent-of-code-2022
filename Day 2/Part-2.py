
# A, X : Rock
# B, Y : Paper
# C, Z : Scissors

# X : Lose
# Y : Draw
# Z : Win

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
            opponentThrow, gameOutcome = line.split(" ")            
            gameState = opponentThrow + gameOutcome

            # Figure out my throw from the game state
            if gameState == "AX":
                myThrow = "Z"
            elif gameState == "AY":
                myThrow = "X"
            elif gameState == "AZ":
                myThrow = "Y"
            elif gameState == "BX":
                myThrow = "X"
            elif gameState == "BY":
                myThrow = "Y"
            elif gameState == "BZ":
                myThrow = "Z"
            elif gameState == "CX":
                myThrow = "Y"
            elif gameState == "CY":
                myThrow = "Z"
            elif gameState == "CZ":
                myThrow = "X"

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