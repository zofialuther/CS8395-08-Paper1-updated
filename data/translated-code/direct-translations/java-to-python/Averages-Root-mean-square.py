def rootMeanSquare(*nums):
    sum = 0.0
    for num in nums:
        sum += num * num
    return (sum / len(nums)) ** 0.5

nums = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
print("The RMS of the numbers from 1 to 10 is", rootMeanSquare(*nums))