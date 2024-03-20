# Passo 18
# Declare uma nova variável chamada shifted. 
# Use a notação de colchetes para acessar o valor de alphabet 
# no índice index e atribua-o à sua nova variável.


text = "Hello World"
shift = 3
print(text.find("W"))
alphabet = "abcdefghijklmnopqrstuvwxyz"
index = alphabet.find(text[0].lower())
print(index)
shifted = alphabet[index]
