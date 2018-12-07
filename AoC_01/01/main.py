def run(file_name, frequency):
    file = open(file_name,"r")
    for number in file:
        frequency += int(number)
    print(frequency)

if __name__ == "__main__":
    file_name = "input_data.txt"
    frequency = 0
    run(file_name, frequency)
