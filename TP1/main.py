import random

def to_bin(text):
    return [format(ord(char), '08b') for char in text]

def to_text(binary_list):
    return ''.join(chr(int(b, 2)) for b in binary_list)

def gen_key_10b():
    return ''.join(random.choice('01') for _ in range(10))

def generate_permutation(size):
    perm = list(range(1, size + 1))
    random.shuffle(perm)
    return perm

def apply_permutation(data, permutation):
    return ''.join(data[i - 1] for i in permutation)

def generate_subkeys(key):
    p10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    permuted_key = apply_permutation(key, p10)

    left_half, right_half = permuted_key[:5], permuted_key[5:]
    left_half_ls1 = left_half[1:] + left_half[0]
    right_half_ls1 = right_half[1:] + right_half[0]
    key_ls1 = left_half_ls1 + right_half_ls1

    p8 = [6, 3, 7, 4, 8, 5, 10, 9]
    k1 = apply_permutation(key_ls1, p8)

    left_half_ls2 = left_half_ls1[2:] + left_half_ls1[:2]
    right_half_ls2 = right_half_ls1[2:] + right_half_ls1[:2]
    key_ls2 = left_half_ls2 + right_half_ls2

    k2 = apply_permutation(key_ls2, p8)

    return k1, k2

def initial_permutation(data):
    ip = [2, 6, 3, 1, 4, 8, 5, 7]
    return apply_permutation(data, ip)

def inverse_permutation(data):
    ip_inverse = [4, 1, 3, 5, 7, 2, 8, 6]
    return apply_permutation(data, ip_inverse)

def feistel_function(right_half, subkey):
    ep = [4, 1, 2, 3, 2, 3, 4, 1]
    expanded_half = apply_permutation(right_half, ep)

    xor_result = ''.join(str(int(b1) ^ int(b2)) for b1, b2 in zip(expanded_half, subkey))

    s0 = [
        ['01', '00', '11', '10'],
        ['11', '10', '01', '00'],
        ['00', '10', '01', '11'],
        ['11', '01', '11', '10']
    ]

    s1 = [
        ['00', '01', '10', '11'],
        ['10', '00', '01', '11'],
        ['11', '00', '01', '00'],
        ['10', '01', '00', '11']
    ]

    def sbox_lookup(bits, sbox):
        row = int(bits[0] + bits[3], 2)
        col = int(bits[1] + bits[2], 2)
        return sbox[row][col]

    left_bits = xor_result[:4]
    right_bits = xor_result[4:]
    s0_result = sbox_lookup(left_bits, s0)
    s1_result = sbox_lookup(right_bits, s1)

    combined = s0_result + s1_result

    p4 = [2, 4, 3, 1]
    return apply_permutation(combined, p4)


def encrypt_block(block, k1, k2):
    permuted_block = initial_permutation(block)

    left_half = permuted_block[:4]
    right_half = permuted_block[4:]

    f_result = feistel_function(right_half, k1)
    left_half = ''.join(str(int(l) ^ int(f)) for l, f in zip(left_half, f_result))

    left_half, right_half = right_half, left_half

    f_result = feistel_function(right_half, k2)
    left_half = ''.join(str(int(l) ^ int(f)) for l, f in zip(left_half, f_result))

    combined = left_half + right_half

    return inverse_permutation(combined)


def main():
    key = gen_key_10b()
    k1, k2 = generate_subkeys(key)

    plaintext = input("Digite o texto para criptografar: ")
    binary_text = to_bin(plaintext)

    encrypted_blocks = [encrypt_block(block, k1, k2) for block in binary_text]
    print("Texto criptografado:", encrypted_blocks)


if __name__ == "__main__":
    main()
