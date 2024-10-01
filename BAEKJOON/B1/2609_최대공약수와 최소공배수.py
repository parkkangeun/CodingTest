# 2024.10.01
# Python

# 최대공약수
def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

# 최소공배수
def lcm(a, b):
    return (a * b) / gcd(a, b)

num01, num02 = map(int, input().split())
print(gcd(num01, num02))
print(int(lcm(num01, num02)))