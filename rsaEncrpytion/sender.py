import math


def prime_factors(number):
    factors = []
    for i in range(2, number):
        while number % i == 0:
            factors.append(i)
            number = number / i
    return factors


def create_public_key():
    # select random prime numbers p and q
    p = 3
    q = 11
    n = p*q
    phi = (p-1)*(q-1)
    # finding e
    e = 0
    print("p: ", p)
    print("q: ", q)
    for i in range(2, phi+1):
        if math.gcd(i, phi) == 1:
            e = i
            break
    return (e, n)


def encrypt(plaintext, public_key):
    e, n = public_key
    if plaintext > n:
        raise ValueError("Plaintext is greater than n")
    print("Public Key: ", public_key)
    return (plaintext**e) % n


plaintext = int(input("Enter the plaintext: "))

print("Cipher text : ", encrypt(plaintext, create_public_key()))
