# 2024.10.04
# Python

string = []
FizzBuzz = ["Fizz", "Buzz", "FizzBuzz"]
cnt = 0
for _ in range(3):
    string.append(input())

for i in string:
    if i not in FizzBuzz:
        num = int(i) + 3 - cnt
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0 and num % 5 != 0:
            print("Fizz")
        elif num % 3 != 0 and num % 5 == 0:
            print("Buzz")
        else:
            print(num)
        break
    else:
        cnt += 1