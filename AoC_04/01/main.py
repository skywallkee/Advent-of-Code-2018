def getGuard(action):
    action = action.split(" ")
    guardId = int(action[3][1:])
    return guardId

def getMinute(action):
    action = action.split(" ")
    time = action[1].split(":")
    time[1] = int(time[1][:len(time[1])-1])
    return time[1]

def getAction(action):
    action = action.split(" ")
    if "begins" in action:
        action = "b"
    elif "falls" in action:
        action = "s"
    else:
        action = "w"
    return action

def getMostSleepyGuardian(GuardianHistory):
    maxHoursAsleep = 0
    mostSleepyGuardian = 0
    for guardian in GuardianHistory:
        hoursAsleep = sum(GuardianHistory[guardian])
        if hoursAsleep > maxHoursAsleep:
            maxHoursAsleep = hoursAsleep
            mostSleepyGuardian = guardian
    return mostSleepyGuardian

def getMostSleepedMinute(GuardianHistory, guardian):
    mostSleepedMinute = 0
    for minute in range(0, 60):
        if GuardianHistory[guardian][minute] > GuardianHistory[guardian][mostSleepedMinute]:
            mostSleepedMinute = minute
    return mostSleepedMinute

def run(file_name):
    file = open(file_name, "r")
    GuardianHistory = {}
    beginSleep = 0
    for action in file:
        if "Guard" in action:
            currentGuard = getGuard(action)
        actionMinute = getMinute(action)
        currentAction = getAction(action)
        if currentGuard not in GuardianHistory:
            GuardianHistory[currentGuard] = []
            for nrMinutes in range(0, 60):
                GuardianHistory[currentGuard].append(0)
        if currentAction == "s":
            beginSleep = actionMinute
        elif currentAction == "w":
            for sleepedMinute in range(beginSleep, actionMinute):
                GuardianHistory[currentGuard][sleepedMinute] += 1

    mostSleepyGuardian = getMostSleepyGuardian(GuardianHistory)
    mostSleepedMinute = getMostSleepedMinute(GuardianHistory, mostSleepyGuardian)
    print(mostSleepyGuardian*mostSleepedMinute)
if __name__ == "__main__":
    file_name = "input_data.txt"
    run(file_name)
