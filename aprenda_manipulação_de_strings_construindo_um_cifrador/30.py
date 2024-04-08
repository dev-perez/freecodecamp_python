# Passo 30
# No final do corpo do seu loop,
# declare uma variável chamada new_index
# e atribua o valor de index + shift a essa variável.


text = "Hello World"
shift = 3
alphabet = "abcdefghijklmnopqrstuvwxyz"
for char in text.lower():
    index = alphabet.find(char)
    print(char, index)
    new_index = index + shift
