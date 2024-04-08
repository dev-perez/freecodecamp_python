# Passo 31
# As strings são imutáveis, o que significa que elas não podem ser alteradas depois de criadas.
# Por exemplo, você pode pensar que o seguinte código
# altera o valor de my_string para a string 'train',
# mas isso não é válido:


# my_string = 'brain'
# my_string[0] = 't'


# Confirme isso usando a notação de colchetes para acessar
# a primeira letra em text e tente alterá-la para um caractere de sua escolha.
# Você verá que a saída desaparece.


text = "Hello World"
text[0] = "R"
shift = 3
alphabet = "abcdefghijklmnopqrstuvwxyz"
for char in text.lower():
    index = alphabet.find(char)
    print(char, index)
    new_index = index + shift
