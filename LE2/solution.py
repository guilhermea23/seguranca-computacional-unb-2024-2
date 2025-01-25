class RSA:
    def __init__(self, p: int, q: int, e: int):
        self.p = p
        self.q = q
        self.e = e
        self.n = p * q
        self.phi_n = (p - 1) * (q - 1)
        self.d = self._modular_inverse(e, self.phi_n)

    def _modular_inverse(self, a: int, m: int):
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        raise ValueError(f"Não existe inverso modular para a={a} e m={m}")

    def encrypt(self, M: int):
        return pow(M, self.e, self.n)

    def decrypt(self, C: int):
        return pow(C, self.d, self.n)

def exercicio1(casos: list[tuple[int, int, int, int]]) -> list[dict]:
    resultados = []
    for case in casos:
        p, q, e, M = case
        rsa = RSA(p, q, e)
        C = rsa.encrypt(M)
        M_decrypted = rsa.decrypt(C)
        resultados.append({"p": p, "q": q, "e": e, "M": M, "n": rsa.n, "d": rsa.d, "C": C, "M_decrypted": M_decrypted})
    return resultados

def exercicio2(casos: list[tuple[int, int, int, int]]) -> list[dict]:
    resultados = []
    for case in casos:
        p, q, e, C = case
        rsa = RSA(p, q, e)
        M_decrypted = rsa.decrypt(C)
        resultados.append({"p": p, "q": q, "e": e, "C": C, "n": rsa.n, "d": rsa.d, "M_decrypted": M_decrypted})
    return resultados

def exercicio3(casos: list[tuple[int, int, int, int]]) -> list[dict]:
    resultados = []
    for case in casos:
        p, q, e, M = case
        rsa = RSA(p, q, e)
        C = rsa.encrypt(M)
        M_decrypted = rsa.decrypt(C)
        resultados.append({"p": p, "q": q, "e": e, "M": M, "n": rsa.n, "d": rsa.d, "C": C, "M_decrypted": M_decrypted})
    return resultados

def exercicio4(casos: list[tuple[int, int, int, str]]) -> list[dict]:
    resultados = []
    for case in casos:
        p, q, e, message = case
        ascii_values = [ord(char) for char in message]
        rsa = RSA(p, q, e)
        encrypted_ascii = [rsa.encrypt(m) for m in ascii_values]
        decrypted_ascii = [rsa.decrypt(c) for c in encrypted_ascii]
        decrypted_message = ''.join(chr(m) for m in decrypted_ascii)
        resultados.append({"Mensagem original": message, "ASCII": ascii_values, "Encriptada": encrypted_ascii, "Decriptada": decrypted_message})
    return resultados

if __name__ == "__main__":
    ex1_cases = [(3, 11, 7, 5), (5, 11, 3, 9), (7, 11, 17, 8), (11, 13, 11, 7), (17, 31, 7, 2)]
    ex2_cases = [(5, 7, 5, 10)]
    ex3_cases = [(11, 23, 3, int("0111001", 2))]
    ex4_cases = [(11, 17, 7, "HELLO")]

    resultados_ex1 = exercicio1(ex1_cases)
    resultados_ex2 = exercicio2(ex2_cases)
    resultados_ex3 = exercicio3(ex3_cases)
    resultados_ex4 = exercicio4(ex4_cases)

    print("\n=== Resultados do Exercício 1 ===")
    for res in resultados_ex1:
        print(f"p={res['p']}, q={res['q']}, e={res['e']}, M={res['M']}, n={res['n']}, d={res['d']}, C={res['C']}, M_decrypted={res['M_decrypted']}")

    print("\n=== Resultados do Exercício 2 ===")
    for res in resultados_ex2:
        print(f"p={res['p']}, q={res['q']}, e={res['e']}, C={res['C']}, n={res['n']}, d={res['d']}, M_decrypted={res['M_decrypted']}")

    print("\n=== Resultados do Exercício 3 ===")
    for res in resultados_ex3:
        print(f"p={res['p']}\nq={res['q']}\ne={res['e']}\nM={res['M']}\nn={res['n']}\nd={res['d']}\nC={res['C']}\nM_decrypted={res['M_decrypted']}")

    print("\n=== Resultados do Exercício 4 ===")
    for res in resultados_ex4:
        print(f"Mensagem original: {res['Mensagem original']}\nASCII: {res['ASCII']}\nEncriptada: {res['Encriptada']}\nDecriptada: {res['Decriptada']}")
