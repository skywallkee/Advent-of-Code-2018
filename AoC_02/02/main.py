def checkStrings(string1, string2):
    differentCharacters = 0
    sameCharacters = ""
    for position in range(0, len(string1)):
        if string1[position] != string2[position]:
            differentCharacters += 1
        else:
            sameCharacters += string1[position]
    if differentCharacters != 1:
        return ""
    return sameCharacters

def run(file_name):
    file = open(file_name,"r")
    listOfWords = []
    result = ""
    for word in file:
        listOfWords.append(word[:len(word)-1])

    for word1 in range(len(listOfWords)-1):
        for word2 in range(word1, len(listOfWords)):
            intersection = checkStrings(listOfWords[word1], listOfWords[word2])
            if intersection != "":
                result += intersection
    print(result)

if __name__ == "__main__":
    file_name = "input_data.txt"
    run(file_name)
