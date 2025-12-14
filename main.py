#Задание 2 списки

numbers = [4, 8, 15, 16, 23, 42]
max_num = max(numbers)
min_num = min(numbers) 
avg = sum(numbers) / len(numbers)
new_numbers = []

for i in range(len(numbers)):
    if numbers[i] > avg:
        new_numbers.append(numbers[i])

print(max_num)
print(min_num)
print(avg)
print(new_numbers)
