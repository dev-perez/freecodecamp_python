# Passo 17
# Remova a última chamada de print(). 
# Em vez de text[0], passe text[0].lower()
# para .find() e veja a saída.


text = "Hello World"
shift = 3
print(text.find("W"))
alphabet = "abcdefghijklmnopqrstuvwxyz"
index = alphabet.find(text[0].lower())
print(index)
