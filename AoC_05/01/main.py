def eliminatePairs(bigWord):
    currentPosition = 0
    while currentPosition < len(bigWord)-1:
        if bigWord[currentPosition].upper() == bigWord[currentPosition+1].upper():
            if bigWord[currentPosition] != bigWord[currentPosition+1]:
                del bigWord[currentPosition]
                del bigWord[currentPosition]
                currentPosition -= 2
        currentPosition += 1
    return bigWord

def run(file_name):
    file = open(file_name, "r")
    bigWord = list(file.read().strip())
    bigWord = eliminatePairs(bigWord)
    print(len(bigWord))
    
if __name__ == "__main__":
    file_name = "input_data.txt"
    run(file_name)
