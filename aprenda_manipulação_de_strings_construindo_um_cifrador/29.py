# Passo 29
# find está novamente retornando -1
# para letras maiúsculas e também para o caractere de espaço.
# Você vai lidar com o espaço mais tarde.

# Por enquanto, em vez de iterar sobre text,
# mude o loop for para iterar sobre text.lower().


text = "Hello World"
shift = 3
alphabet = "abcdefghijklmnopqrstuvwxyz"
for char in text.lower():
    index = alphabet.find(char)
    print(char, index)
