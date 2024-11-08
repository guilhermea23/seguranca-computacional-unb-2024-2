# Definindo a chave secreta
secret_key = 'seguro'
# Mapeando os índices da chave ordenada para reordenação das colunas
columns = {index: char for index, char in enumerate(sorted(secret_key))}
# Invertendo o dicionário para facilitar a busca da posição original de cada caractere
column_order = {v: i for i, v in columns.items()}

# Obtendo a mensagem e removendo espaços
mensagem = input("Qual mensagem deve ser cifrada?\n ").replace(" ", "")
# Tamanho da chave e cálculo do número de colunas e linhas da matriz
num_cols = len(secret_key)
num_rows = (len(mensagem) + num_cols - 1) // num_cols  # Arredonda para cima

# Preenchendo a matriz com a mensagem e espaços em branco
grid = [['' for _ in range(num_cols)] for _ in range(num_rows)]
for i, char in enumerate(mensagem):
    row, col = divmod(i, num_cols)
    grid[row][col] = char

# Reorganizando as colunas da matriz com base na ordem da chave
cifrado = []
for i in sorted(column_order.values()):
    for row in grid:
        if row[i]:  # Ignora células vazias
            cifrado.append(row[i])

# Convertendo a lista para a string final cifrada
cipher_text = ''.join(cifrado)
print("Mensagem cifrada:", cipher_text)
