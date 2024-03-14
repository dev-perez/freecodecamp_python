# Passo 13
# O primeiro tipo de cifra que você vai construir 
# é chamado de cifra de César. 
# Especificamente, você vai pegar cada letra na sua mensagem, 
# encontrar sua posição no alfabeto, pegar a letra localizada 
# após 3 posições e substituir a letra original pela nova letra.

# Comece encontrando a posição da primeira letra na string. 
# Uma maneira é chamar o método de string 
# .find() na string que você deseja analisar:

# text.find('W')
# Acima, 'W' em maiúsculo é o caractere que você deseja localizar 
# dentro da string armazenada na variável de texto. 
# O método retornará 6, que é o índice do caractere 'W' 
# dentro da string armazenada na variável de texto.

# No final do seu código, chame .find() na sua string de alfabeto 
# e passe text[0] para o método. 
# Note que um método é apenas uma função que pertence 
# a um objeto (você aprenderá mais sobre isso em outro projeto).


text = "hello world"
print(text.find("w"))
alphabet = "abcdefghijklmnopqrstuvwxyz"
print(alphabet.find(text[0]))
