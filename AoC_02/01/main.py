def run(file_name):
    numberOfWords = {"two letters":0, "three letters":0}
    file = open(file_name,"r")
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    hasTwoLetters = False
    hasThreeLetters = False
    for word in file:
        hasTwoLetters = False
        hasThreeLetters = False
        for letter in alphabet:
            letterFrequency = word.count(letter)
            if letterFrequency == 2:
                hasTwoLetters = True
            if letterFrequency == 3:
                hasThreeLetters = True
        if hasTwoLetters == True:
            numberOfWords["two letters"] += 1
        if hasThreeLetters == True:
            numberOfWords["three letters"] += 1
    print(numberOfWords["two letters"]*numberOfWords["three letters"])

if __name__ == "__main__":
    file_name = "input_data.txt"
    run(file_name)
