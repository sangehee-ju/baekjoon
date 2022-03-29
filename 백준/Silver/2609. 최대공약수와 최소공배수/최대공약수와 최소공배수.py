import sys

n, m = map(int, sys.stdin.readline().split())


# 유클리드 호제법

# 2개의 자연수 a,b에 대해 a를 b로 나눈 나머지를 r이라 하면(a<b)
# a와 b의 최대 공약수는 b와 r의 최대공약수와 같다.
# ==> b를 r로 나눈 나머지 r'를 구하는 과정을 나머지가 0이 될 때까지 기다림.

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


# 최소공배수는 a,b의 곱을 a,b의 최대 공약수로 나누면 나온다.
def lcm(a, b):
    return int(a * b / gcd(a, b))


print(gcd(n, m))
print(lcm(n, m))
