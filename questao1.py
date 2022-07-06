num = int(input("Digite o valor inicial \n"))
index = 0
array = [0,1]
while array[index+1] <= num:
    soma = array[index]+array[index+1]
    array.append(soma)
    index += 1
if(array.__contains__(num)):
    print("O número pertence à sequencia")
else:
    print("o número não pertence à sequência")
print(array)
    