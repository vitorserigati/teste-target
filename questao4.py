text = input("Digite a frase que deseja inverter: \n")

print(text[::-1])


reverse = ""
length = len(text)
index = length -1
while index >= 0:
    reverse += text[index]  
    index -=1

print(reverse)



#Neste exercício resolvi fazer de duas formas. Uma da forma que o python nos permite fazer.
#E a outra, com um while, para inverter a string