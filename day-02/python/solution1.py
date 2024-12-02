from os import confstr
import sys

file = sys.argv[1]

result = 0

with open(file, "r") as f:
    while line := f.readline():
        x = list(map(int, line.split()))
        result += 1
        isPositiveDiff = True
        for idx,n in enumerate(x):
            if idx == 0:
                continue

            # get the diffrence
            diff = n - x[idx-1]
    
            # check if the difference is gt 3 or lt 1
            if abs(diff) > 3 or abs(diff) < 1:
                result -= 1
                break

            # this is the first diff to determint if the list is inc or dec
            if idx == 1:
                if diff < 0:
                    isPositiveDiff = False
                if diff > 0:
                    isPositiveDiff = True
            else:
                if isPositiveDiff != (diff > 0):
                    result -= 1
                    break


print(result)
