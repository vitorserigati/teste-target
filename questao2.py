import json
with open('faturamento.json', 'r') as faturamento:
    list = json.load(faturamento)
maior_valor = 0
maior_dia = ''
menor_dia = ''
menor_valor = list[0]['valor']
soma = 0
index = 0
dia_fatura = 0
for i in list:
    if(list[index]['valor']>0):
        soma +=list[index]['valor']
        dia_fatura+=1

    index+=1

media = soma/dia_fatura

index = 0

for i in list:
    if(list[index]['valor']>media):
        print(f"O dia {list[index]['dia']} teve um faturamento maior do que a média, que é de: {media}!")
    if(list[index]['valor']>maior_valor):
        maior_dia = list[index]['dia']
        maior_valor=list[index]['valor']
    if(list[index]['valor'] > 0 and list[index]['valor'] < menor_valor):
        menor_dia = list[index]['dia']
        menor_valor = list[index]['valor']
        
    index +=1
print(' ')
print(f"O dia: {maior_dia}, foi o de maior lucro, com um valor de: {maior_valor}")
print(' ')
print(f"O dia: {menor_dia}, foi o de menor lucro, com um valor de: {menor_valor}")