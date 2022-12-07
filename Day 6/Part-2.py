if __name__ == "__main__":
    with open("Input.txt") as f:
        for line in f:
            charBuffer = []
            charCount = 0
            for char in line:
                charCount += 1
                charBuffer.append(char)
                if len(charBuffer) > 14:
                    charBuffer.pop(0)
                    if len(set(charBuffer)) == len(charBuffer):
                        break
                
            print(charCount)
