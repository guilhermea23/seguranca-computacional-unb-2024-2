from string import ascii_uppercase
from collections import Counter

# Dicionários de mapeamento entre letras e números
alphabet_dict = {letter: index_of + 1 for index_of, letter in enumerate(ascii_uppercase)}
numeric_dict = {index_of + 1: letter for index_of, letter in enumerate(ascii_uppercase)}


# Função de cifragem
def encrypt(text: str, k: int = 3):
    text_ciphered = ' '.join(str(alphabet_dict[letter]) for letter in text.upper() if letter in alphabet_dict)
    text_mixed = mix(text_ciphered, k)
    return encrypt_cipher(text_mixed)


# Função para aplicar o deslocamento
def mix(text_numeric: str, how: int):
    text_shifted = ' '.join(str((int(number) + how) % 26) for number in text_numeric.split())
    return text_shifted


# Função para converter o texto de volta para letras
def encrypt_cipher(text: str):
    text_ciphered = ''.join(numeric_dict.get(int(number), '') for number in text.split())
    return text_ciphered


# Função de decifragem
def decrypt(text_cifrado: str, k: int):
    text_numeric = ' '.join(str((int(number) - k) % 26) for number in text_cifrado.split())
    return encrypt_cipher(text_numeric)


# Função para o ataque por força bruta
def forca_bruta(text_cifrado: str):
    print("Tentativas de força bruta para cada deslocamento:")
    for k in range(1, 26):  # Tentar todos os deslocamentos possíveis
        tentativa = decrypt(text_cifrado, k)
        print(f"Deslocamento {k}: {tentativa}")


# Função para o ataque por distribuição de frequência
def ataque_frequencia(text_cifrado: str):
    # Conta a frequência das letras no texto cifrado
    frequencias = Counter(text_cifrado)
    letra_mais_comum = frequencias.most_common(1)[0][0]  # Letra mais frequente no texto cifrado

    # Assumindo que a letra mais comum no texto cifrado corresponde a 'E' (letra mais frequente em inglês)
    letra_suspeita = 'E'
    deslocamento_suspeito = (alphabet_dict[letra_mais_comum] - alphabet_dict[letra_suspeita]) % 26

    # Decifra o texto usando o deslocamento calculado
    mensagem_decifrada = decrypt(text_cifrado, deslocamento_suspeito)
    print(f"\nDeslocamento suspeito pelo ataque de frequência: {deslocamento_suspeito}")
    print("Mensagem decifrada (baseada em distribuição de frequência):", mensagem_decifrada)
    return mensagem_decifrada


if __name__ == "__main__":
    # Parte de cifragem
    plaintext = input("Entre com a mensagem que deseja cifrar: \n").upper()
    mensagem_cifrada = encrypt(plaintext)
    print("\nMensagem cifrada:", mensagem_cifrada)

    # Escolha do método de ataque
    print("\nEscolha o método de ataque para decifrar a mensagem:")
    print("1 - Ataque por força bruta")
    print("2 - Ataque por distribuição de frequência")
    escolha = input("Digite 1 ou 2: ")

    if escolha == '1':
        print("\nResultado do ataque por força bruta:")
        forca_bruta(mensagem_cifrada)
    elif escolha == '2':
        print("\nResultado do ataque por distribuição de frequência:")
        ataque_frequencia(mensagem_cifrada)
    else:
        print("Escolha inválida.")
