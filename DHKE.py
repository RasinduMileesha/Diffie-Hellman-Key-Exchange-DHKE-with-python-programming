import random

def generate_prime_and_primitive_root(bits=10): #used just 10 bits, we can increase for more secure
    # randomly taking a random prime number
    prime = random.randint(2 ** (bits - 1), 2 ** bits - 1)

    # Find a primitive root modulo prime
    primitive_root = 2
    while pow(primitive_root, (prime - 1) // 2, prime) == 1 or pow(primitive_root, prime - 1, prime) != 1:
        primitive_root = random.randint(2, prime - 1)
    #pow used for exponential oprtations
    return prime, primitive_root


# Find Tim's private and public keys
def tim_key_gen(prime, primitive_root):
    tim_private_key = random.randint(1, prime - 1)
    tim_public_key = pow(primitive_root, tim_private_key, prime)
    return tim_private_key, tim_public_key


# Find Stephen's private and public keys
def stephen_key_gen(prime, primitive_root):
    stephen_private_key = random.randint(1, prime - 1)
    stephen_public_key = pow(primitive_root, stephen_private_key, prime)
    return stephen_private_key, stephen_public_key


# Find the shared key
def find_shared_key(private_key, other_public_key, prime):
    shared_key = pow(other_public_key, private_key, prime)
    return shared_key



def main():

    prime, primitive_root = generate_prime_and_primitive_root()


    tim_private_key, tim_public_key = tim_key_gen(prime, primitive_root)


    stephen_private_key, stephen_public_key = stephen_key_gen(prime, primitive_root)


    tim_shared_key = find_shared_key(tim_private_key, stephen_public_key, prime)
    stephen_shared_key = find_shared_key(stephen_private_key, tim_public_key, prime)

    # Check the shared keys are same
    assert tim_shared_key == stephen_shared_key

    return prime, primitive_root, tim_private_key, tim_public_key, stephen_private_key, stephen_public_key, tim_shared_key


# Run the main
prime, primitive_root, tim_private_key, tim_public_key, stephen_private_key, stephen_public_key, shared_key = main()


print("Prime:", prime)
print("Primitive Root:", primitive_root)
print("Tim's Private Key:", tim_private_key)
print("Tim's Public Key:", tim_public_key)
print("Stephen's Private Key:", stephen_private_key)
print("Stephen's Public Key:", stephen_public_key)
print("Shared Key:", shared_key)
