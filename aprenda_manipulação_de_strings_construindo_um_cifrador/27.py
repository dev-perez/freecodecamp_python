# Passo 27
# Dentro do loop for, antes de imprimir o caractere atual,
# declare uma variável chamada index e
# atribua o valor retornado por alphabet.find(char) a essa variável.


text = "Hello World"
shift = 3
alphabet = "abcdefghijklmnopqrstuvwxyz"
for char in text:
    index = alphabet.find(char)
    print(char)
