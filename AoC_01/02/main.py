def run(file_name, frequency):
    frequencies = {}
    while True:
        file = open(file_name,"r")
        for number in file:
            if frequency in frequencies:
                break
            else:
                frequencies[frequency] = 1
            frequency += int(number)
        if frequency in frequencies:
            break
    print(frequency)

if __name__ == "__main__":
    file_name = "input_data.txt"
    frequency = 0
    run(file_name, frequency)
