sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19843.53
estados = ["SP", "RJ", "MG","ES", "Outros"]
lucros=[67836.43, 36678.66, 29229.88, 27165.48, 19849.53]

soma = sp+rj+mg+es+outros
index = 0   
print(f"Lucro total da empresa: {soma}")
print("O Lucro de cada estado foi: \n")
for i in lucros:
    media = (i * 100) / soma    
    print(f"{estados[index]} = {lucros[index]} com um lucro de: " +f"{media}"[:5]+"%")
    index +=1
