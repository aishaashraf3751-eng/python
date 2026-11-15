for i in range(1, 11):
    print(f"23 x {i} = {23 * i}")

n = int(input("Enter the number of rows: " ))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

total_sum = 0
num = 1

while num <= 10:
    total_sum += num
    num += 1

print(f"The sum of numbers from 1 to 10 is: {total_sum}")