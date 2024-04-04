# Passo 28
# Atualmente, a função print() está recebendo um único argumento char,
# mas ela pode receber vários argumentos, separados por uma vírgula.

# Adicione um segundo argumento para print(char)
# para que ele imprima o caractere e seu índice dentro do alfabeto.


text = "Hello World"
shift = 3
alphabet = "abcdefghijklmnopqrstuvwxyz"
for char in text:
    index = alphabet.find(char)
    print(char, index)
