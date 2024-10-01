# 2024.10.01
# Python

def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a
def lcm(a, b):
    return (a * b) / gcd(a, b)

num01, num02 = map(int, input().split())
print(gcd(num01, num02))
print(int(lcm(num01, num02)))