totalTrials = 1000
switchSuccess = 0
staySuccess = 0
switchFailure = 0
stayFailure = 0

for i in range(1, totalTrials+1):
    random_num1 = random.uniform(0, 1)
    if random_num1 <= 0.67:
        switchSuccess += 1
    else:
        switchFailure += 1
    random_num2 = random.uniform(0, 1)
    if random_num2 <= 0.34:
        staySuccess += 1
    else:
        stayFailure += 1

switchSuccessRate = (switchSuccess / totalTrials) * 100
staySuccessRate = (staySuccess / totalTrials) * 100
print(switchSuccessRate)
print(staySuccessRate)