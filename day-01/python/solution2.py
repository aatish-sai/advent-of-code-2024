
arr_a = []
arr_b = []

# file = "./../input_sample.txt"
file = "./../input_p1.txt"

with open(file, 'r') as f:
    while line := f.readline():
        x, y = map(int,line.split())
        arr_a.append(x)
        arr_b.append(y)

sorted_arr_a = sorted(arr_a)
sorted_arr_b = sorted(arr_b)

result = 0
value_count_dict = {}

for x in sorted_arr_b:
    if x in value_count_dict:
        value_count_dict[x] += 1
    else:
        value_count_dict[x] = 1

for x in sorted_arr_a:
    if x in value_count_dict:
        result += x * value_count_dict[x]

print(result)

