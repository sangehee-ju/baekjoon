import sys

r = sys.stdin.readline

n, k = map(int, r().split())
p = 1000000007


def factorial(x):
    t = 1
    for i in range(2, x+1):
        t = (t * i) % p

    return t


def solution(n, k):
    if k == 0:
        return 1
    elif k == 1:
        return n

    temp = solution(n, k // 2)
    if k % 2:
        return temp * temp * n % p
    else:
        return temp * temp % p


# 페르마의 소정리 이용 ==> 조합공식 곱셈 형태로 변형
# ※ 페르마의 소정리
# a^p mod p = a mod p
# 즉, a^(p-1) ≡ 1 (mod p) = a * a^(p-2) ≡ 1(mod p)
# ===> a^(p-2) = 1/a
# ※
# 위 정리에 따라 ==>  1/(r!(n-r)!) = (r!(n-r)!)^(1000000007 - 2) ( p = 1000000007 )
# 즉, nCr = n! * (r!(n-r)!)^(1000000007 - 2)


top = factorial(n)
bottom = factorial(k) * factorial(n - k) % p
print(top * solution(bottom, p - 2) % p)
