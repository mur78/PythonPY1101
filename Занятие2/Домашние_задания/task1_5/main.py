from string import ascii_lowercase, ascii_uppercase, digits
from random import sample
n = ascii_lowercase + ascii_uppercase + digits

def gen_value():
    z = sample(n,8)
    print(z)
    return z


if __name__ == "__main__":
    print(n)
    gen_value()
