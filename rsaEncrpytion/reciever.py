def find_private_key(public_key, p, q):
    e, n = public_key
    phi = (p-1)*(q-1)
    d = 0
    for i in range(2, phi+1):
        if (i*e) % phi == 1:
            d = i
            break
    return (d, n)


def decrypt(ciphertext, private_key):
    d, n = private_key
    if ciphertext > n:
        raise ValueError("ciphertext is greater than n")
    return (ciphertext**d) % n


ciphertext = int(input("Enter the ciphertext: "))
p = int(input("Enter the value of p: "))
q = int(input("Enter the value of q: "))
# input public key tuple
public_key = tuple(map(int, input("Enter the public key: ").split()))

print("Decrypted text: ", decrypt(ciphertext,
      find_private_key(public_key, p, q)))
