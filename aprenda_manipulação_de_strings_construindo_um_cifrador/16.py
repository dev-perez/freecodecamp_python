# Passo 16
# .find() retorna o índice do caractere correspondente dentro da string.
# Se o caractere não for encontrado, ele retorna -1.
# Como você pode ver, o primeiro caractere em texto,
# 'H' maiúsculo, não é encontrado, já que o alfabeto contém apenas letras minúsculas.

# Você pode transformar uma string em sua equivalente em minúsculas com o método
# .lower().
# Adicione outra chamada de print() para imprimir text.lower() e veja a saída.


text = "Hello World"
shift = 3
print(text.find("W"))
alphabet = "abcdefghijklmnopqrstuvwxyz"
index = alphabet.find(text[0])
print(index)
print(text.lower())
