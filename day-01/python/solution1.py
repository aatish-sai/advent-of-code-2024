arr_a = []
arr_b:list[int] = []

# file = "./../input_sample.txt"
file = "./../input_p1.txt"

with open(file, "r") as f:
    while line := f.readline():
        x, y = map(int, line.split())
        arr_a.append(x)
        arr_b.append(y)

sorted_arr_a = sorted(arr_a)
sorted_arr_b = sorted(arr_b)

result = 0
for a, b in zip(sorted_arr_a, sorted_arr_b):
    result += abs(a - b)

print(result)
